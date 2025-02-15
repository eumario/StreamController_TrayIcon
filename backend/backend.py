from streamcontroller_plugin_tools import BackendBase
import trayicon
import os
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GLib
from loguru import logger as log


class StreamControllerTrayIcon(trayicon.TrayIcon):
    MenuPath = "/dev/eumario/StreamController_TrayIcon/Menu"
    IndicatorPath = "/org/ayatana/NotificationItem/dev_eumario_StreamController_TrayIcon"
    AppId = "dev.eumario.StreamController.TrayIcon"

    def __init__(self, menu, icon):
        self.menu = menu
        super().__init__(self.menu, self.MenuPath, self.IndicatorPath, self.AppId, "StreamController")
        self.set_icon(icon)
        self.set_tooltip("StreamController")


class TrayIconBackend(BackendBase):
    def __init__(self):
        super().__init__()

        self.loop = GLib.MainLoop()
        asset_path = os.path.join(self.frontend.PATH, "backend", "assets", "icon.png")
        log.debug(f"Icon Path: {asset_path}")
        self.menu = trayicon.Menu()
        self.menu.add_menu_item(1, "Show", callback=self._handle_show)
        self.menu.add_menu_item(2, menu_type="separator")
        self.menu.add_menu_item(3, "Store", callback=self._handle_store)
        self.menu.add_menu_item(4,"Quit", callback=self._handle_quit)

        self.tray = StreamControllerTrayIcon(self.menu, asset_path)

        log.info("Showing tray icon.")
        self.loop.run()
        log.info("GLib loop exited.")

    # TODO: need to be implemented in gl.app
    # def _handle_settings(self, _icon, _item):
    #     log.debug("Showing Settings from TrayIcon")
    #     self.frontend.handle_settings()
    #
    # def _handle_about(self, _icon, _item):
    #     log.debug("Showing About from TrayIcon")
    #     self.frontend.handle_about()

    def _handle_show(self):
        log.debug("Showing MainWindow from TrayIcon")
        self.frontend.handle_reopen()

    def _handle_store(self):
        log.debug("Showing Store from TrayIcon")
        self.frontend.handle_store()

    def _handle_quit(self):
        log.debug("Quitting App from TrayIcon")
        self.frontend.handle_quit()

    def on_disconnect(self, conn):
        log.debug("Shutting down Tray loop")
        self.loop.quit()
        super().on_disconnect(conn)

backend = TrayIconBackend()