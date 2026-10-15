from textual.app import App
from textual.binding import Binding
from ui.home_screen import HomeScreen
from ui.start_screen import StartScreen


class ChatroomApp(App):
    SCREENS = {
        "start": StartScreen,
        "home": HomeScreen
    }

    BINDINGS = [
        Binding(key="ctrl+q", action="quit", description="Quit the app")
    ]

    theme = "gruvbox"

    ENABLE_COMMAND_PALETTE = False

    AUTO_FOCUS = False

    def on_mount(self):
        self.push_screen("start")