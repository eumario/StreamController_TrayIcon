# Import StreamController modules

from src.backend.PluginManager.PluginBase import PluginBase
from src.backend.PluginManager.ActionHolder import ActionHolder
from src.windows.mainWindow.headerBar import HeaderBar

import globals as gl

import os

class PluginTrayIcon(PluginBase):
    def __init__(self):
        super().__init__()

        backend_path = os.path.join(self.PATH, "backend", "backend.py")
        self.launch_backend(backend_path=backend_path, open_in_terminal=False, venv_path=os.path.join(self.PATH, "backend", ".venv"))
        self.wait_for_backend(5)

        self.register(
            plugin_name = "TrayIcon",
            github_repo = "https://github.com/eumario/StreamController_TrayIcon",
            plugin_version = "0.1.0",
            app_version = "1.5.0-beta6"
        )

    def handle_reopen(self):
        gl.app.on_reopen([],[])

    def handle_quit(self):
        gl.app.on_quit([],[])

    def handle_store(self):
        gl.app.open_store(None)

    # TODO: Need to be implemented in gl.app
    def handle_settings(self):
        pass

    def handle_about(self):
        pass