from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical, Horizontal
from textual.widgets import Footer, Button, Static
from widgets import NonToggleHeader
from pyfiglet import Figlet


class StartScreen(App):

    ENABLE_COMMAND_PALETTE = False

    AUTO_FOCUS = False

    BINDINGS = [
        Binding(key="ctrl+q", action="quit", description="Quit the app")
    ]

    CSS = """
    Screen {
        align: center middle;
    }

    HeaderIcon {
        display: none;
    }

    .container-start {
        width: 100%;
        height: auto;
    }

    .logo {
        width: 100%;
        height: auto;
        text-align: center;
    }
    
    .button-row {
        width: 100%;
        height: auto;
        align: center middle;
    }

    Button {
        width: auto;
        padding: 1;
        border: round $secondary;
        background: transparent;
    }
    
    Button:focus{
    
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
        self.theme = "gruvbox"
        self.title = "Chatroom"
        self.sub_title = "Made by naokimon and Yoru_VSV"


if __name__ == "__main__":
    app = StartScreen()
    app.run()
