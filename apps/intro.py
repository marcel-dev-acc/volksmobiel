from typing import Any
from constants import margin

class Intro:

    def __init__(self) -> None:
        pass

    def show(self, route: str, canvas: Any, device: Any | None) -> None:
        """Method used for rendering the screen"""
        with canvas(device) as draw:
            draw.text((0 + margin, 0 + margin),
                        "VOLKSMOBIEL", fill="white", font_size=9)
            draw.text((0 + margin, 10 + margin),
                        "The phone for you", fill="white", font_size=9)