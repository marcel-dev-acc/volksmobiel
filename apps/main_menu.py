from typing import Any
from luma.core.render import canvas

from apps.routes import Routes
from constants import margin, text_color, font_size, hightlight_selected

class MainMenu:

    def __init__(self) -> None:
        self.options = [
            "Call",
            "Text",
            "Contacts",
            "Calculator",
            "Calendar",
            "Turn off"
        ]

    def show(self, route: str, canvas: canvas, device: Any | None, active_option: int) -> None:
        """Method used for rendering the screen"""
        if route == Routes().main_menu:
            with canvas(device) as draw:
                for idx, option in enumerate(self.options):
                    draw.text((0 + margin, ((10 * idx) + margin)),
                            f"{idx + 1}: {option}", fill=text_color, font_size=font_size)
                    if idx == active_option:
                        draw.rectangle(
                            xy=(0, (10 * idx), device.width - margin,
                                (10 * idx) + 10 + 2 * margin),
                            outline=hightlight_selected
                        )

    def action(self, **kwargs) -> None:
        """Method to handle key presses"""
        if (
            kwargs["app"] is None or
            kwargs["route"] is None or
            kwargs["key"] is None
        ):
            raise Exception("Missing arguments in Intro().action")