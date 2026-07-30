from __future__ import annotations

from pathlib import Path
import sys
import threading

from PySide6.QtCore import QObject, Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QFormLayout,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QPlainTextEdit,
    QSizePolicy,
    QStackedWidget,
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
from avto_vinchick_tg.dv_bot import DvActionSettings
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
    steps = ["Прокси", "Telegram", "Бот", "Фильтры", "Запуск"]

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("AvtoVinchick TG")
        icon = app_icon_path()
        if icon.exists():
            self.setWindowIcon(QIcon(str(icon)))
        self.resize(1120, 780)
        self.setMinimumSize(960, 680)
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
        self.setStyleSheet(APP_STYLE)
        root = QWidget()
        root.setObjectName("AppRoot")
        self.setCentralWidget(root)
        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(18, 16, 18, 16)
        root_layout.setSpacing(14)

        header = self._build_header()
        root_layout.addWidget(header)

        body = QHBoxLayout()
        body.setSpacing(14)
        root_layout.addLayout(body, 1)

        self.step_list = QListWidget()
        self.step_list.setObjectName("StepList")
        self.step_list.setFixedWidth(185)
        for index, title in enumerate(self.steps, start=1):
            item = QListWidgetItem(f"{index}. {title}")
            item.setSizeHint(item.sizeHint().expandedTo(item.sizeHint()))
            self.step_list.addItem(item)
        self.step_list.currentRowChanged.connect(self.set_step)
        body.addWidget(self.step_list)

        content = QVBoxLayout()
        content.setSpacing(12)
        body.addLayout(content, 1)

        self.stack = QStackedWidget()
        self.stack.addWidget(self._proxy_page())
        self.stack.addWidget(self._telegram_page())
        self.stack.addWidget(self._bot_page())
        self.stack.addWidget(self._filters_page())
        self.stack.addWidget(self._run_page())
        content.addWidget(self.stack, 1)

        nav = QHBoxLayout()
        nav.setSpacing(10)
        self.status_label = QLabel("Готово")
        self.status_label.setObjectName("StatusText")
        nav.addWidget(self.status_label, 1)
        self.back_button = QPushButton("Назад")
        self.back_button.clicked.connect(self.previous_step)
        self.next_button = QPushButton("Дальше")
        self.next_button.setObjectName("PrimaryButton")
        self.next_button.clicked.connect(self.next_step)
        nav.addWidget(self.back_button)
        nav.addWidget(self.next_button)
        content.addLayout(nav)

        self.step_list.setCurrentRow(0)
        self.set_step(0)

    def _build_header(self) -> QWidget:
        header = QFrame()
        header.setObjectName("Header")
        layout = QHBoxLayout(header)
        layout.setContentsMargins(18, 14, 18, 14)
        title_col = QVBoxLayout()
        title = QLabel("AvtoVinchick TG")
        title.setObjectName("AppTitle")
        subtitle = QLabel("Фильтрация анкет Дайвинчика и отправка подходящих сообщений в вашего Telegram-бота")
        subtitle.setObjectName("MutedText")
        title_col.addWidget(title)
        title_col.addWidget(subtitle)
        layout.addLayout(title_col, 1)

        layout.addWidget(self.badge(f"Приложение v{APP_VERSION}"))
        layout.addWidget(self.badge(f"Ядро v{CORE_VERSION}"))

        self.app_update_button = QPushButton("")
        self.app_update_button.setObjectName("UpdateButton")
        self.app_update_button.clicked.connect(self.download_app_update)
        self.app_update_button.hide()
        layout.addWidget(self.app_update_button)

        self.core_update_button = QPushButton("")
        self.core_update_button.setObjectName("DisabledUpdateButton")
        self.core_update_button.setEnabled(False)
        self.core_update_button.hide()
        layout.addWidget(self.core_update_button)
        return header

    def _proxy_page(self) -> QWidget:
        page = self.page("1. Прокси", "SOCKS5H для Telegram и Bot API")
        self.proxy_url = self.line("SOCKS5H proxy", placeholder="socks5h://127.0.0.1:1080")
        page.layout().addWidget(self.proxy_url)
        return page

    def _telegram_page(self) -> QWidget:
        page = self.page("2. Telegram аккаунт", "Вход в пользовательский аккаунт Telegram")
        form = QFormLayout()
        form.setSpacing(12)
        self.phone = self.raw_line("Телефон", placeholder="+79990000000")
        self.code = QLineEdit()
        self.code.setPlaceholderText("Код из Telegram")
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Пароль 2FA")
        send_code = QPushButton("Отправить код")
        submit_code = QPushButton("Войти по коду")
        submit_password = QPushButton("Войти с 2FA")
        send_code.clicked.connect(self.send_code)
        submit_code.clicked.connect(self.submit_code)
        submit_password.clicked.connect(self.submit_password)
        form.addRow("Телефон", self.phone)
        form.addRow(send_code)
        form.addRow("Код", self.code)
        form.addRow(submit_code)
        form.addRow("2FA пароль", self.password)
        form.addRow(submit_password)
        box = self.panel()
        box.layout().addLayout(form)
        page.layout().addWidget(box)
        return page

    def _bot_page(self) -> QWidget:
        page = self.page("3. Бот и источник", "Куда отправлять прошедшие фильтр анкеты")
        grid = QGridLayout()
        grid.setSpacing(12)
        self.bot_token = self.line("Bot token", password=True, placeholder="123456:ABC...")
        self.notify_chat_id = self.line("Ваш chat_id", placeholder="Нажмите Найти chat_id")
        self.source_chat = self.line("Чат Дайвинчика", placeholder="LeomatchBot")
        grid.addWidget(self.bot_token, 0, 0)
        grid.addWidget(self.notify_chat_id, 0, 1)
        grid.addWidget(self.source_chat, 1, 0, 1, 2)
        page.layout().addLayout(grid)

        buttons = QHBoxLayout()
        for title, handler in [
            ("Сохранить", self.save_config),
            ("Тест бота", self.test_bot),
            ("Найти chat_id", self.find_chat_id),
        ]:
            button = QPushButton(title)
            button.clicked.connect(handler)
            buttons.addWidget(button)
        buttons.addStretch(1)
        page.layout().addLayout(buttons)
        return page

    def _filters_page(self) -> QWidget:
        page = self.page("4. Фильтры", "Правила отбора анкет")
        text_grid = QGridLayout()
        text_grid.setSpacing(12)
        self.banned_text = self.textbox("Запрещенные слова/фразы")
        self.required_text = self.textbox("Обязательные слова/фразы")
        self.banned_regex = self.textbox("Запрещенные regex")
        self.required_regex = self.textbox("Обязательные regex")
        text_grid.addWidget(self.banned_text, 0, 0)
        text_grid.addWidget(self.required_text, 0, 1)
        text_grid.addWidget(self.banned_regex, 1, 0)
        text_grid.addWidget(self.required_regex, 1, 1)
        page.layout().addLayout(text_grid, 1)

        numeric = QGroupBox("Числовые ограничения")
        numeric_layout = QGridLayout(numeric)
        numeric_layout.setSpacing(10)
        self.min_words = self.small_line("Мин. слов")
        self.max_words = self.small_line("Макс. слов")
        self.min_chars = self.small_line("Мин. символов")
        self.max_chars = self.small_line("Макс. символов")
        self.min_age = self.small_line("Мин. возраст")
        self.max_age = self.small_line("Макс. возраст")
        for index, widget in enumerate(
            [self.min_words, self.max_words, self.min_chars, self.max_chars, self.min_age, self.max_age]
        ):
            numeric_layout.addWidget(widget, index // 3, index % 3)
        page.layout().addWidget(numeric)

        flags = QGroupBox("Дополнительно")
        flags_layout = QGridLayout(flags)
        flags_layout.setSpacing(8)
        self.reject_without_age = QCheckBox("Отсеивать без возраста")
        self.require_photo = QCheckBox("Требовать фото/медиа")
        self.reject_links = QCheckBox("Отсеивать ссылки")
        self.reject_mentions = QCheckBox("Отсеивать @mentions")
        self.send_rejects_to_log = QCheckBox("Логировать отказы")
        for index, widget in enumerate(
            [
                self.reject_without_age,
                self.require_photo,
                self.reject_links,
                self.reject_mentions,
                self.send_rejects_to_log,
            ]
        ):
            flags_layout.addWidget(widget, index // 3, index % 3)
        page.layout().addWidget(flags)
        return page

    def _run_page(self) -> QWidget:
        page = self.page("5. Запуск", "Старт слушателя и журнал работы")
        dv_box = QGroupBox("Поведение ДВ")
        dv_layout = QGridLayout(dv_box)
        dv_layout.setSpacing(10)
        self.accepted_action = QComboBox()
        self.accepted_action.addItem("Только переслать мне", "notify")
        self.accepted_action.addItem("Переслать мне и лайкнуть: 1", "like")
        self.accepted_action.addItem("Переслать мне и лайкнуть с посланием: 2", "like_message")
        self.accepted_action.addItem("Переслать мне и пропустить: 3", "skip")
        self.auto_skip_rejected = QCheckBox("Неподходящие анкеты пропускать командой 3")
        self.auto_open_found = QCheckBox("На 'Нашел анкеты. Показать?' отвечать 1")
        self.ignore_ads = QCheckBox("Рекламу и Premium-сообщения игнорировать")
        self.forward_likes = QCheckBox("Лайки и взаимные симпатии пересылать мне")
        dv_layout.addWidget(QLabel("Подходящая анкета"), 0, 0)
        dv_layout.addWidget(self.accepted_action, 0, 1, 1, 2)
        for index, widget in enumerate(
            [
                self.auto_skip_rejected,
                self.auto_open_found,
                self.ignore_ads,
                self.forward_likes,
            ],
        ):
            dv_layout.addWidget(widget, 1 + index // 2, index % 2)
        page.layout().addWidget(dv_box)

        actions = QHBoxLayout()
        start = QPushButton("Запуск")
        start.setObjectName("PrimaryButton")
        stop = QPushButton("Стоп")
        start.clicked.connect(self.start)
        stop.clicked.connect(self.stop)
        actions.addWidget(start)
        actions.addWidget(stop)
        actions.addStretch(1)
        page.layout().addLayout(actions)

        log_box = QGroupBox("Лог")
        log_layout = QVBoxLayout(log_box)
        self.log = QPlainTextEdit()
        self.log.setReadOnly(True)
        self.log.setPlaceholderText("События появятся здесь")
        log_layout.addWidget(self.log)
        page.layout().addWidget(log_box, 1)
        return page

    def set_step(self, index: int) -> None:
        if index < 0:
            return
        self.stack.setCurrentIndex(index)
        self.back_button.setEnabled(index > 0)
        self.next_button.setText("Готово" if index == len(self.steps) - 1 else "Дальше")
        self.status_label.setText(self.steps[index])

    def next_step(self) -> None:
        index = self.stack.currentIndex()
        self.save_config()
        if index < len(self.steps) - 1:
            self.step_list.setCurrentRow(index + 1)

    def previous_step(self) -> None:
        index = self.stack.currentIndex()
        if index > 0:
            self.step_list.setCurrentRow(index - 1)

    def current_config(self) -> AppConfig:
        return AppConfig(
            phone=self.phone.text().strip(),
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
            dv_actions=DvActionSettings(
                auto_skip_rejected=self.auto_skip_rejected.isChecked(),
                accepted_action=str(self.accepted_action.currentData() or "notify"),
                auto_open_found=self.auto_open_found.isChecked(),
                ignore_ads=self.ignore_ads.isChecked(),
                forward_likes=self.forward_likes.isChecked(),
                auto_decline_like_prompts=False,
            ),
            send_rejects_to_log=self.send_rejects_to_log.isChecked(),
        )

    def load_config(self) -> None:
        config = AppConfig.load()
        self.phone.setText(config.phone)
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
        self.auto_skip_rejected.setChecked(config.dv_actions.auto_skip_rejected)
        self.auto_open_found.setChecked(config.dv_actions.auto_open_found)
        self.ignore_ads.setChecked(config.dv_actions.ignore_ads)
        self.forward_likes.setChecked(config.dv_actions.forward_likes)
        self.set_combo_value(self.accepted_action, config.dv_actions.accepted_action)

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
        self.core_update_button.setText(f"Новое ядро v{latest}")
        self.core_update_button.show()
        self.append_log(f"Вышла новая версия ядра tg-api-zapret: {latest}. Автообновление ядра отключено.")

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
                installer_path = download_release_asset(release, config.proxy_url)
                install_downloaded_release(installer_path)
            except Exception as exc:
                self.bridge.app_update_failed.emit(str(exc))
                return
            self.bridge.message.emit("Обновление скачано. Приложение закроется и перезапустится.")
            self.bridge.app_update_ready.emit()

        threading.Thread(target=worker, daemon=True).start()

    def show_app_update_failed(self, error: str) -> None:
        self.append_log(f"Обновление не выполнено: {error}")
        if self.latest_app_release:
            self.app_update_button.setText(f"Доступно обновление v{self.latest_app_release.version}")
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
                QMessageBox.information(
                    self,
                    "Нет updates",
                    "Сначала напишите любое сообщение своему боту.",
                )
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
    def page(title: str, subtitle: str) -> QWidget:
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        title_label = QLabel(title)
        title_label.setObjectName("PageTitle")
        subtitle_label = QLabel(subtitle)
        subtitle_label.setObjectName("MutedText")
        layout.addWidget(title_label)
        layout.addWidget(subtitle_label)
        return widget

    @staticmethod
    def panel() -> QFrame:
        frame = QFrame()
        frame.setObjectName("Panel")
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)
        return frame

    @staticmethod
    def badge(text: str) -> QLabel:
        label = QLabel(text)
        label.setObjectName("Badge")
        label.setAlignment(Qt.AlignCenter)
        return label

    @staticmethod
    def raw_line(label: str, *, placeholder: str = "", password: bool = False) -> QLineEdit:
        edit = QLineEdit()
        edit.setAccessibleName(label)
        edit.setPlaceholderText(placeholder)
        if password:
            edit.setEchoMode(QLineEdit.Password)
        return edit

    @staticmethod
    def line(label: str, *, password: bool = False, placeholder: str = "") -> QGroupBox:
        box = QGroupBox(label)
        layout = QVBoxLayout(box)
        edit = MainWindow.raw_line(label, placeholder=placeholder, password=password)
        layout.addWidget(edit)
        return box

    @staticmethod
    def small_line(label: str) -> QFrame:
        frame = QFrame()
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(QLabel(label))
        layout.addWidget(QLineEdit())
        frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        return frame

    @staticmethod
    def textbox(label: str) -> QGroupBox:
        box = QGroupBox(label)
        layout = QVBoxLayout(box)
        edit = QPlainTextEdit()
        edit.setMinimumHeight(105)
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

    @staticmethod
    def set_combo_value(combo: QComboBox, value: str) -> None:
        index = combo.findData(value)
        combo.setCurrentIndex(index if index >= 0 else 0)


APP_STYLE = """
QWidget#AppRoot {
    background: #f5f7fb;
    color: #172033;
    font-family: "Segoe UI";
    font-size: 10pt;
}
QFrame#Header {
    background: #ffffff;
    border: 1px solid #dfe5ef;
    border-radius: 8px;
}
QFrame#Panel,
QGroupBox {
    background: #ffffff;
    border: 1px solid #dfe5ef;
    border-radius: 8px;
    margin-top: 10px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 12px;
    padding: 0 6px;
    color: #526073;
}
QLabel#AppTitle {
    font-size: 20pt;
    font-weight: 700;
    color: #111827;
}
QLabel#PageTitle {
    font-size: 17pt;
    font-weight: 700;
    color: #111827;
}
QLabel#MutedText,
QLabel#StatusText {
    color: #64748b;
}
QLabel#Badge {
    background: #eef2f7;
    border: 1px solid #d8e0eb;
    border-radius: 8px;
    color: #334155;
    padding: 7px 10px;
}
QListWidget#StepList {
    background: #ffffff;
    border: 1px solid #dfe5ef;
    border-radius: 8px;
    padding: 8px;
    outline: 0;
}
QListWidget#StepList::item {
    border-radius: 7px;
    padding: 12px 10px;
    margin: 2px;
    color: #334155;
}
QListWidget#StepList::item:selected {
    background: #e7f0ff;
    color: #0f4aa1;
}
QLineEdit,
QPlainTextEdit {
    background: #fbfdff;
    border: 1px solid #cfd8e5;
    border-radius: 7px;
    padding: 8px;
    selection-background-color: #2f80ed;
}
QLineEdit:focus,
QPlainTextEdit:focus {
    border-color: #2f80ed;
    background: #ffffff;
}
QPushButton {
    background: #ffffff;
    border: 1px solid #cfd8e5;
    border-radius: 7px;
    padding: 9px 14px;
    color: #172033;
}
QPushButton:hover {
    background: #f1f5f9;
}
QPushButton:disabled {
    color: #94a3b8;
    background: #eef2f7;
}
QPushButton#PrimaryButton {
    background: #1f6feb;
    border-color: #1f6feb;
    color: #ffffff;
    font-weight: 600;
}
QPushButton#PrimaryButton:hover {
    background: #195ec8;
}
QPushButton#UpdateButton {
    background: #0f766e;
    border-color: #0f766e;
    color: #ffffff;
}
QPushButton#DisabledUpdateButton {
    background: #fff7ed;
    border-color: #fed7aa;
    color: #9a3412;
}
QCheckBox {
    spacing: 8px;
    color: #334155;
}
"""


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
