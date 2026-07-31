from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import webbrowser

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QApplication, QMenu, QMessageBox, QSystemTrayIcon

from avto_vinchick_tg.service import AppService
from avto_vinchick_tg.web_server import WebServer


class TrayApplication:
    def __init__(self, app: QApplication) -> None:
        self.app = app
        self.service = AppService()
        self.server = WebServer(self.service)
        self.server.start()
        self.tray = QSystemTrayIcon(QIcon(str(app_icon_path())), app)
        self.tray.setToolTip("AvtoVinchickTG")
        self.tray.setContextMenu(self.build_menu())
        self.tray.activated.connect(self.on_activated)
        self.tray.show()
        self.service.log(f"Web UI запущен: {self.server.url}")
        self.open_page()

    def build_menu(self) -> QMenu:
        menu = QMenu()
        open_action = QAction("Открыть страницу", menu)
        open_action.triggered.connect(self.open_page)
        status_action = QAction("Статус", menu)
        status_action.triggered.connect(self.show_status)
        restart_action = QAction("Перезапуск приложения", menu)
        restart_action.triggered.connect(self.restart_app)
        stop_action = QAction("Остановить слушатель", menu)
        stop_action.triggered.connect(self.service.stop)
        quit_action = QAction("Выход", menu)
        quit_action.triggered.connect(self.quit)
        menu.addAction(open_action)
        menu.addAction(status_action)
        menu.addSeparator()
        menu.addAction(stop_action)
        menu.addAction(restart_action)
        menu.addSeparator()
        menu.addAction(quit_action)
        return menu

    def open_page(self) -> None:
        webbrowser.open(self.server.url)

    def show_status(self) -> None:
        state = self.service.snapshot()
        running = "запущен" if state["running"] else "остановлен"
        QMessageBox.information(
            None,
            "AvtoVinchickTG статус",
            (
                f"Web UI: {self.server.url}\n"
                f"Слушатель: {running}\n"
                f"Приложение: v{state['app_version']}\n"
                f"Ядро: v{state['core_version']}"
            ),
        )

    def restart_app(self) -> None:
        executable = Path(sys.executable).resolve()
        args = [str(executable)] if getattr(sys, "frozen", False) else [str(executable), *sys.argv]
        subprocess.Popen(args, cwd=str(executable.parent), close_fds=True)
        self.quit()

    def on_activated(self, reason: QSystemTrayIcon.ActivationReason) -> None:
        if reason == QSystemTrayIcon.DoubleClick:
            self.open_page()

    def quit(self) -> None:
        self.service.stop()
        self.server.stop()
        self.tray.hide()
        self.app.quit()


def main() -> None:
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    icon = app_icon_path()
    if icon.exists():
        app.setWindowIcon(QIcon(str(icon)))
    TrayApplication(app)
    sys.exit(app.exec())


def app_icon_path() -> Path:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
    return base / "assets" / "AvtoVinchickTG.ico"
