from textual.app import ComposeResult
from textual.containers import Vertical, Horizontal
from textual.screen import Screen
from textual.widgets import Footer, Button, Static
from ui.widgets import NonToggleHeader
from pyfiglet import Figlet


class StartScreen(Screen):

    CSS = """
    Screen {
        align: center middle;
    }

    HeaderIcon {
        display: none;
    }

    .container-start {
        height: 100%;
        align: center middle;
    }

    .logo {
        width: 100%;
        text-align: center;
    }

    
    .button-row {
        height: auto;
        align: center middle;
    }

    Button {
        padding: 0;
        border: round $secondary;
        background: transparent;
    }
    
    Button:focus{
        text-style: none;
    }
    
    Button:hover {
        pointer: crosshair;
    }
    """

    def compose(self) -> ComposeResult:
        yield NonToggleHeader(icon="")

        figlet = Figlet(font="ansi_shadow")

        yield Vertical(
            Static(
                figlet.renderText("CHATROOM"),
                classes="logo"
            ),
            Horizontal(
                Button("Start Chatroom."),
                classes="button-row"
            ),
            classes="container-start"
        )

        yield Footer()

    def on_mount(self) -> None:
        self.title = "Chatroom"
        self.sub_title = "Made by naokimon and Yoru_VSV"

    def on_button_pressed(self, event: Button.Pressed):
        self.app.push_screen("home")
