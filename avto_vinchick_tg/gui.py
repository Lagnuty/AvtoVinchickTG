from __future__ import annotations

from pathlib import Path
import sys
import threading

from PySide6.QtGui import QIcon
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QPlainTextEdit,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

from avto_vinchick_tg import __version__ as APP_VERSION
from avto_vinchick_tg.app_update import (
    AppRelease,
    download_release_asset,
    fetch_latest_app_release,
    install_downloaded_release,
)
from avto_vinchick_tg.core_update import fetch_latest_core_version, is_newer_version
from avto_vinchick_tg.filters import FilterSettings
from avto_vinchick_tg.runner import VinchikRunner
from avto_vinchick_tg.settings import AppConfig
from tg_api_zapret import __version__ as CORE_VERSION


class LogBridge(QObject):
    message = Signal(str)
    core_update = Signal(str)
    app_update = Signal(object)
    app_update_failed = Signal(str)
    app_update_ready = Signal()


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("AvtoVinchick TG")
        icon = app_icon_path()
        if icon.exists():
            self.setWindowIcon(QIcon(str(icon)))
        self.resize(1060, 760)
        self.bridge = LogBridge()
        self.bridge.message.connect(self.append_log)
        self.bridge.core_update.connect(self.show_core_update)
        self.bridge.app_update.connect(self.show_app_update)
        self.bridge.app_update_failed.connect(self.show_app_update_failed)
        self.bridge.app_update_ready.connect(self.finish_app_update)
        self.latest_app_release: AppRelease | None = None
        self.runner = VinchikRunner(self.bridge.message.emit)
        self._build()
        self.load_config()
        self.check_core_update()
        self.check_app_update()

    def _build(self) -> None:
        root = QWidget()
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)

        version_row = QHBoxLayout()
        layout.addLayout(version_row)
        version_row.addWidget(QLabel(f"AvtoVinchick TG v{APP_VERSION}"))
        version_row.addWidget(QLabel(f"Ядро tg-api-zapret v{CORE_VERSION}"))
        version_row.addStretch(1)
        self.app_update_button = QPushButton("")
        self.app_update_button.clicked.connect(self.download_app_update)
        self.app_update_button.hide()
        version_row.addWidget(self.app_update_button)
        self.core_update_button = QPushButton("")
        self.core_update_button.setEnabled(False)
        self.core_update_button.hide()
        version_row.addWidget(self.core_update_button)

        top = QGridLayout()
        layout.addLayout(top)
        self.phone = self.line("Телефон")
        self.bot_token = self.line("Bot token", password=True)
        self.notify_chat_id = self.line("Ваш chat_id для уведомлений")
        self.source_chat = self.line("Чат Дайвинчика")
        self.proxy_url = self.line("SOCKS5H proxy")
        for index, widget in enumerate(
            [self.phone, self.bot_token, self.notify_chat_id, self.source_chat, self.proxy_url]
        ):
            top.addWidget(widget, index // 3, index % 3)

        buttons = QHBoxLayout()
        layout.addLayout(buttons)
        for title, handler in [
            ("Сохранить", self.save_config),
            ("Тест бота", self.test_bot),
            ("Найти chat_id", self.find_chat_id),
        ]:
            button = QPushButton(title)
            button.clicked.connect(handler)
            buttons.addWidget(button)

        splitter = QSplitter()
        layout.addWidget(splitter, 1)

        filters = QWidget()
        filter_layout = QVBoxLayout(filters)
        text_grid = QGridLayout()
        filter_layout.addLayout(text_grid, 1)
        self.banned_text = self.textbox("Запрещенные слова/фразы")
        self.required_text = self.textbox("Обязательные слова/фразы")
        self.banned_regex = self.textbox("Запрещенные regex")
        self.required_regex = self.textbox("Обязательные regex")
        text_grid.addWidget(self.banned_text, 0, 0)
        text_grid.addWidget(self.required_text, 0, 1)
        text_grid.addWidget(self.banned_regex, 1, 0)
        text_grid.addWidget(self.required_regex, 1, 1)

        numeric = QGroupBox("Числовые фильтры")
        numeric_layout = QHBoxLayout(numeric)
        self.min_words = self.small_line("Мин. слов")
        self.max_words = self.small_line("Макс. слов")
        self.min_chars = self.small_line("Мин. символов")
        self.max_chars = self.small_line("Макс. символов")
        self.min_age = self.small_line("Мин. возраст")
        self.max_age = self.small_line("Макс. возраст")
        for widget in [
            self.min_words,
            self.max_words,
            self.min_chars,
            self.max_chars,
            self.min_age,
            self.max_age,
        ]:
            numeric_layout.addWidget(widget)
        filter_layout.addWidget(numeric)

        flags = QGroupBox("Дополнительно")
        flags_layout = QHBoxLayout(flags)
        self.reject_without_age = QCheckBox("Отсеивать без возраста")
        self.require_photo = QCheckBox("Требовать фото")
        self.reject_links = QCheckBox("Отсеивать ссылки")
        self.reject_mentions = QCheckBox("Отсеивать @")
        self.send_rejects_to_log = QCheckBox("Логировать отказы")
        for widget in [
            self.reject_without_age,
            self.require_photo,
            self.reject_links,
            self.reject_mentions,
            self.send_rejects_to_log,
        ]:
            flags_layout.addWidget(widget)
        filter_layout.addWidget(flags)
        splitter.addWidget(filters)

        right = QWidget()
        right_layout = QVBoxLayout(right)
        actions = QGroupBox("Управление")
        actions_layout = QFormLayout(actions)
        self.code = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        send_code = QPushButton("1. Отправить код")
        submit_code = QPushButton("2. Войти по коду")
        submit_password = QPushButton("Войти с 2FA")
        start = QPushButton("Запуск")
        stop = QPushButton("Стоп")
        send_code.clicked.connect(self.send_code)
        submit_code.clicked.connect(self.submit_code)
        submit_password.clicked.connect(self.submit_password)
        start.clicked.connect(self.start)
        stop.clicked.connect(self.stop)
        actions_layout.addRow(send_code)
        actions_layout.addRow("Код", self.code)
        actions_layout.addRow(submit_code)
        actions_layout.addRow("2FA пароль", self.password)
        actions_layout.addRow(submit_password)
        actions_layout.addRow(start)
        actions_layout.addRow(stop)
        right_layout.addWidget(actions)

        log_box = QGroupBox("Лог")
        log_layout = QVBoxLayout(log_box)
        self.log = QPlainTextEdit()
        self.log.setReadOnly(True)
        log_layout.addWidget(self.log)
        right_layout.addWidget(log_box, 1)
        splitter.addWidget(right)
        splitter.setSizes([650, 360])

    def current_config(self) -> AppConfig:
        return AppConfig(
            phone=self.phone.findChild(QLineEdit).text().strip(),
            bot_token=self.bot_token.findChild(QLineEdit).text().strip(),
            notify_chat_id=self.notify_chat_id.findChild(QLineEdit).text().strip(),
            source_chat=self.source_chat.findChild(QLineEdit).text().strip() or "LeomatchBot",
            proxy_url=self.proxy_url.findChild(QLineEdit).text().strip(),
            filters=FilterSettings(
                banned_text=self.text_lines(self.banned_text),
                required_text=self.text_lines(self.required_text),
                banned_regex=self.text_lines(self.banned_regex),
                required_regex=self.text_lines(self.required_regex),
                min_words=self.int_value(self.min_words),
                max_words=self.int_value(self.max_words),
                min_chars=self.int_value(self.min_chars),
                max_chars=self.int_value(self.max_chars),
                min_age=self.int_value(self.min_age),
                max_age=self.int_value(self.max_age),
                reject_without_age=self.reject_without_age.isChecked(),
                require_photo=self.require_photo.isChecked(),
                reject_links=self.reject_links.isChecked(),
                reject_mentions=self.reject_mentions.isChecked(),
            ),
            send_rejects_to_log=self.send_rejects_to_log.isChecked(),
        )

    def load_config(self) -> None:
        config = AppConfig.load()
        self.set_line(self.phone, config.phone)
        self.set_line(self.bot_token, config.bot_token)
        self.set_line(self.notify_chat_id, config.notify_chat_id)
        self.set_line(self.source_chat, config.source_chat)
        self.set_line(self.proxy_url, config.proxy_url)
        self.set_text(self.banned_text, "\n".join(config.filters.banned_text))
        self.set_text(self.required_text, "\n".join(config.filters.required_text))
        self.set_text(self.banned_regex, "\n".join(config.filters.banned_regex))
        self.set_text(self.required_regex, "\n".join(config.filters.required_regex))
        for widget, value in [
            (self.min_words, config.filters.min_words),
            (self.max_words, config.filters.max_words),
            (self.min_chars, config.filters.min_chars),
            (self.max_chars, config.filters.max_chars),
            (self.min_age, config.filters.min_age),
            (self.max_age, config.filters.max_age),
        ]:
            self.set_line(widget, str(value or ""))
        self.reject_without_age.setChecked(config.filters.reject_without_age)
        self.require_photo.setChecked(config.filters.require_photo)
        self.reject_links.setChecked(config.filters.reject_links)
        self.reject_mentions.setChecked(config.filters.reject_mentions)
        self.send_rejects_to_log.setChecked(config.send_rejects_to_log)

    def check_core_update(self) -> None:
        config = self.current_config()

        def worker() -> None:
            latest = fetch_latest_core_version(config.proxy_url)
            if is_newer_version(latest, CORE_VERSION):
                self.bridge.core_update.emit(latest or "")

        threading.Thread(target=worker, daemon=True).start()

    def check_app_update(self) -> None:
        config = self.current_config()

        def worker() -> None:
            try:
                release = fetch_latest_app_release(APP_VERSION, config.proxy_url)
            except Exception as exc:
                self.bridge.message.emit(f"Не удалось проверить обновление приложения: {exc}")
                return
            if release:
                self.bridge.app_update.emit(release)

        threading.Thread(target=worker, daemon=True).start()

    def show_core_update(self, latest: str) -> None:
        self.core_update_button.setText(f"Обновить ядро нельзя: вышла v{latest}")
        self.core_update_button.show()
        self.append_log(f"Вышла новая версия ядра tg-api-zapret: {latest}. Автообновление отключено.")

    def show_app_update(self, release: AppRelease) -> None:
        self.latest_app_release = release
        self.app_update_button.setText(f"Доступно обновление v{release.version}")
        self.app_update_button.setEnabled(True)
        self.app_update_button.show()
        self.append_log(f"Доступно обновление приложения: v{release.version}.")

    def download_app_update(self) -> None:
        release = self.latest_app_release
        if not release:
            return
        self.app_update_button.setEnabled(False)
        self.app_update_button.setText(f"Скачиваю v{release.version}...")
        config = self.current_config()

        def worker() -> None:
            try:
                archive_path = download_release_asset(release, config.proxy_url)
                install_downloaded_release(archive_path)
            except Exception as exc:
                self.bridge.app_update_failed.emit(str(exc))
                return
            self.bridge.message.emit("Обновление скачано. Приложение закроется и перезапустится.")
            self.bridge.app_update_ready.emit()

        threading.Thread(target=worker, daemon=True).start()

    def show_app_update_failed(self, error: str) -> None:
        self.append_log(f"Обновление не выполнено: {error}")
        if self.latest_app_release:
            self.app_update_button.setText(
                f"Доступно обновление v{self.latest_app_release.version}"
            )
            self.app_update_button.setEnabled(True)

    def finish_app_update(self) -> None:
        QApplication.quit()

    def save_config(self) -> None:
        self.current_config().save()
        self.append_log("Настройки сохранены.")

    def send_code(self) -> None:
        self.save_config()
        self.runner.login_send_code(self.current_config())

    def submit_code(self) -> None:
        self.runner.login_submit_code(self.code.text())

    def submit_password(self) -> None:
        self.runner.login_submit_password(self.password.text())

    def test_bot(self) -> None:
        self.save_config()
        from avto_vinchick_tg.bot_api import BotApi

        config = self.current_config()
        try:
            me = BotApi(config.bot_token, proxy_url=config.proxy_url).get_me()
            self.append_log(f"Бот отвечает: @{me.get('result', {}).get('username', 'unknown')}")
        except Exception as exc:
            QMessageBox.critical(self, "Ошибка Bot API", str(exc))

    def find_chat_id(self) -> None:
        self.save_config()
        from avto_vinchick_tg.bot_api import BotApi

        config = self.current_config()
        try:
            updates = BotApi(config.bot_token, proxy_url=config.proxy_url).get_updates()
            items = updates.get("result") or []
            if not items:
                QMessageBox.information(self, "Нет updates", "Сначала напишите любое сообщение своему боту.")
                return
            message = items[-1].get("message") or items[-1].get("edited_message") or {}
            chat_id = str((message.get("chat") or {}).get("id") or "")
            if not chat_id:
                QMessageBox.information(self, "Нет chat_id", "В последнем update не найден чат.")
                return
            self.set_line(self.notify_chat_id, chat_id)
            self.save_config()
            self.append_log(f"chat_id найден: {chat_id}")
        except Exception as exc:
            QMessageBox.critical(self, "Ошибка Bot API", str(exc))

    def start(self) -> None:
        config = self.current_config()
        if not config.bot_token or not config.notify_chat_id:
            QMessageBox.critical(self, "Нет данных", "Укажите bot token и chat_id для уведомлений.")
            return
        self.save_config()
        self.runner.start(config)

    def stop(self) -> None:
        self.runner.stop()

    def append_log(self, message: str) -> None:
        self.log.appendPlainText(message.rstrip())

    @staticmethod
    def line(label: str, *, password: bool = False) -> QGroupBox:
        box = QGroupBox(label)
        layout = QVBoxLayout(box)
        edit = QLineEdit()
        if password:
            edit.setEchoMode(QLineEdit.Password)
        layout.addWidget(edit)
        return box

    @staticmethod
    def small_line(label: str) -> QFrame:
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QLabel(label))
        layout.addWidget(QLineEdit())
        return frame

    @staticmethod
    def textbox(label: str) -> QGroupBox:
        box = QGroupBox(label)
        layout = QVBoxLayout(box)
        edit = QPlainTextEdit()
        layout.addWidget(edit)
        return box

    @staticmethod
    def text_lines(box: QGroupBox) -> list[str]:
        text = box.findChild(QPlainTextEdit).toPlainText()
        return [line.strip() for line in text.splitlines() if line.strip()]

    @staticmethod
    def int_value(frame: QFrame) -> int:
        try:
            return max(0, int(frame.findChild(QLineEdit).text().strip() or 0))
        except ValueError:
            return 0

    @staticmethod
    def set_line(container: QWidget, value: str) -> None:
        container.findChild(QLineEdit).setText(value)

    @staticmethod
    def set_text(box: QGroupBox, value: str) -> None:
        box.findChild(QPlainTextEdit).setPlainText(value)


def main() -> None:
    app = QApplication(sys.argv)
    icon = app_icon_path()
    if icon.exists():
        app.setWindowIcon(QIcon(str(icon)))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def app_icon_path() -> Path:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
    return base / "assets" / "AvtoVinchickTG.ico"
