from typing import Any
from luma.core.render import canvas

from apps.routes import Routes
from constants import margin, back_option, text_color, font_size, hightlight_selected

class Sms:

    def __init__(self) -> None:
        self.options = [
            ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l", "."],
            ["z", "x", "c", "v", "b", "n", "m", ",", "(", ")"],
            ["._.", back_option],
        ]

    def show(self, route: str, canvas: canvas, device: Any | None, active_option: int) -> None:
        """Method used for rendering the screen"""
        if route == Routes().sms:
            with canvas(device) as draw:
                draw.text((0 + margin, 0 + margin),
                        "> _", fill=text_color, font_size=font_size)

                for idx, row in enumerate(self.options):
                    for jdx, option in enumerate(row):
                        draw.text((10 * jdx + margin, ((10 * (idx + 1)) + margin)),
                                f"{option}", fill=text_color, font_size=font_size)
                        num_cols = len(self.options[0])
                        row_idx = active_option // num_cols
                        col_idx = active_option % num_cols
                        if idx == row_idx and jdx == col_idx:
                            x0 = 10 * jdx # (top)-left
                            y0 = 10 * idx + 10 + margin # top-(left)
                            x1 = 10 * jdx + 10 # (bottom)-right
                            y1 = 10 * idx + 10 * 2 + margin # bottom-(right)
                            draw.rectangle(
                                xy=(x0, y0, x1, y1),
                                outline=hightlight_selected
                            )