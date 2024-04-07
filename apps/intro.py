from typing import Any
from pynput.keyboard import KeyCode, Key

from apps.main_menu import MainMenu
from apps.routes import Routes
from constants import margin, text_color, font_size

class Intro:

    def __init__(self) -> None:
        self.options = [Routes().turn_off]

    def show(self, **kwargs) -> None:
        """Method used for rendering the screen"""
        if (
            kwargs["route"] is None or
            kwargs["canvas"] is None or
            kwargs["device"] is None
        ):
            raise Exception("Missing arguments in Intro().show")
        
        route: str = kwargs["route"]
        canvas: Any = kwargs["canvas"]
        device: Any | None = kwargs["device"]
        
        if route == Routes().intro:
            with canvas(device) as draw:
                draw.text((0 + margin, 0 + margin),
                            "VOLKSMOBIEL", fill=text_color, font_size=font_size)
                draw.text((0 + margin, 10 + margin),
                            "The phone for you", fill=text_color, font_size=font_size)
                
    def action(self, **kwargs) -> None:
        """Method to handle key presses"""
        if (
            kwargs["app"] is None or
            kwargs["route"] is None or
            kwargs["key"] is None
        ):
            raise Exception("Missing arguments in Intro().action")
        
        app: Any = kwargs["app"]
        route: str = kwargs["route"]
        key: KeyCode | Key | None = kwargs["canvas"]

        if route == Routes().intro and key == Key.enter:
            app.options = MainMenu().options
            app.route = Routes().main_menu