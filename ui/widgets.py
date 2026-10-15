from textual.widgets import Header

class NonToggleHeader(Header):

    def on_click(self, event) -> None:
        event.prevent_default()