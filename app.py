import time
from pynput.keyboard import Listener, KeyCode, Key
from luma.core.render import canvas

from demo_opts import get_device

from constants import margin

from apps.routes import Routes
from apps.intro import Intro

class App:

    def __init__(self) -> None:
        self.state_changed = True
        self.route = Routes().intro
        self.prev_route = Routes().intro
        self.active_option = 0
        self.options = [
            "Turn off"
        ]
        self.main_menu_opts = [
            "Call",
            "Text",
            "Contacts",
            "Calculator",
            "Calendar",
            "Turn off"
        ]
        self.text_opts = [
            ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
            ["a", "s", "d", "f", "g", "h", "j", "k", "l", "."],
            ["z", "x", "c", "v", "b", "n", "m", ",", "(", ")"],
            ["_", "<<"],
        ]
        self.calculator_opts = [
            ["1", "2", "3", "+"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "x"],
            ["/", "=", "", "<<"],
        ]

    def on_key_press(self, key: KeyCode | Key | None) -> None:
        """Handle the key press for the main menu."""
        if key == Key.up and self.active_option > 0:
            self.state_changed = True
            self.active_option -= 1
        elif key == Key.down:
            if isinstance(self.options[0], list): # Checking if it's a 2D array
                # For a 2D array transform to a 1D array
                one_d_array = [element for sublist in self.options for element in sublist]
                if self.active_option < len(one_d_array) - 1:
                    self.state_changed = True
                    self.active_option += 1
            else:
                # For a 1D array
                if self.active_option < len(self.options) - 1:
                    self.state_changed = True
                    self.active_option += 1
        elif key == Key.enter:
            self.state_changed = True
            is_back = False
            # Checking if it's a 2D array
            if isinstance(self.options[0], list):
                # For a 2D array transform to a 1D array
                one_d_array = [element for sublist in self.options for element in sublist]
                if one_d_array[self.active_option] == "Back":
                    self.route = self.prev_route
                    is_back = True
            else:
                # For a 1D array
                if self.options[self.active_option] == "Back":
                    self.route = self.prev_route
                    is_back = True

            if is_back and self.route == "Main menu":
                self.active_option = 0
                self.options = self.main_menu_opts

            if not is_back:
                if self.route == "Main menu":
                    self.route = self.options[self.active_option]
                    self.prev_route = "Main menu"
                    if self.route == "Text":
                        self.active_option = 0
                        self.options = self.text_opts
                    if self.route == "Calculator":
                        self.active_option = 0
                        self.options = self.calculator_opts
                elif self.route == "Intro":
                    self.options = self.main_menu_opts
                    self.route = "Main menu"
        elif key == Key.esc:
            self.state_changed = True
            self.route = "Exit"


    def main(self) -> None:
        """Main UI Loop"""
        listener = Listener(self.on_key_press)
        listener.start()

        while True:

            if self.state_changed and self.route == Routes().intro:
                self.state_changed = False
                Intro().show(
                    route=self.route,
                    canvas=canvas,
                    device=device
                )

            elif self.state_changed and self.route == "Main menu":
                self.state_changed = False
                with canvas(device) as draw:
                    for idx, option in enumerate(self.options):
                        draw.text((0 + margin, ((10 * idx) + margin)),
                                  f"{idx + 1}: {option}", fill="white", font_size=9)
                        if idx == self.active_option:
                            draw.rectangle(
                                xy=(0, (10 * idx), device.width - margin,
                                    (10 * idx) + 10 + 2 * margin),
                                outline="white"
                            )

            elif self.state_changed and self.route == "Calculator":
                self.state_changed = False
                with canvas(device) as draw:
                    draw.text((0 + margin, 0 + margin),
                              "> _", fill="white", font_size=9)

                    for idx, row in enumerate(self.options):
                        for jdx, option in enumerate(row):
                            draw.text((10 * jdx + margin, ((10 * (idx + 1)) + margin)),
                                    f"{option}", fill="white", font_size=9)
                            num_cols = len(self.options[0])
                            row_idx = self.active_option // num_cols
                            col_idx = self.active_option % num_cols
                            if idx == row_idx and jdx == col_idx:
                                x0 = 10 * jdx # (top)-left
                                y0 = 10 * idx + 10 + margin # top-(left)
                                x1 = 10 * jdx + 10 # (bottom)-right
                                y1 = 10 * idx + 10 * 2 + margin # bottom-(right)
                                draw.rectangle(
                                    xy=(x0, y0, x1, y1),
                                    outline="white"
                                )

            elif self.state_changed and self.route == "Text":
                self.state_changed = False
                with canvas(device) as draw:
                    draw.text((0 + margin, 0 + margin),
                              "> _", fill="white", font_size=9)

                    for idx, row in enumerate(self.options):
                        for jdx, option in enumerate(row):
                            draw.text((10 * jdx + margin, ((10 * (idx + 1)) + margin)),
                                    f"{option}", fill="white", font_size=9)
                            num_cols = len(self.options[0])
                            row_idx = self.active_option // num_cols
                            col_idx = self.active_option % num_cols
                            if idx == row_idx and jdx == col_idx:
                                x0 = 10 * jdx # (top)-left
                                y0 = 10 * idx + 10 + margin # top-(left)
                                x1 = 10 * jdx + 10 # (bottom)-right
                                y1 = 10 * idx + 10 * 2 + margin # bottom-(right)
                                draw.rectangle(
                                    xy=(x0, y0, x1, y1),
                                    outline="white"
                                )

            elif self.state_changed and self.route == "Exit":
                break



if __name__ == "__main__":
    device = get_device()
    app = App()
    app.main()
