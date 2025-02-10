from streamcontroller_plugin_tools import BackendBase

import os

os.environ["PYSTRAY_BACKEND"] = "gtk"

import pystray
from loguru import logger as log
from PIL import Image

class TrayIconBackend(BackendBase):
    def __init__(self):
        super().__init__()

        asset_path = os.path.join(self.frontend.PATH, "backend", "assets", "icon.png")
        log.debug(f"Icon Path: {asset_path}")
        self.icon = Image.open(asset_path)
        res = self.icon.load()
        log.debug(f"load() == None: {res == None}")

        self.tray = pystray.Icon("StreamController", icon=self.icon,
                                 menu = pystray.Menu(
                                     pystray.MenuItem("Show", self._handle_show),
                                     #pystray.MenuItem("Settings", self._handle_settings),
                                     pystray.MenuItem("Store", self._handle_store),
                                     #pystray.MenuItem("About", self._handle_about),
                                     pystray.MenuItem("Quit", self._handle_quit)
                                 ))
        log.info("Showing tray icon.")
        self.tray.run()

    # TODO: need to be implemented in gl.app
    # def _handle_settings(self, _icon, _item):
    #     log.debug("Showing Settings from TrayIcon")
    #     self.frontend.handle_settings()
    #
    # def _handle_about(self, _icon, _item):
    #     log.debug("Showing About from TrayIcon")
    #     self.frontend.handle_about()

    def _handle_show(self, _icon, _item):
        log.debug("Showing MainWindow from TrayIcon")
        self.frontend.handle_reopen()

    def _handle_store(self, _icon, _item):
        log.debug("Showing Store from TrayIcon")
        self.frontend.handle_store()

    def _handle_quit(self, _icon, _item):
        log.debug("Quitting App from TrayIcon")
        self.frontend.handle_quit()

    def on_disconnect(self, conn):
        log.debug("Shutting down Tray loop")
        self.tray.stop()
        super().on_disconnect(conn)

backend = TrayIconBackend()