import time
from pynput.keyboard import Listener, KeyCode, Key
from luma.core.render import canvas
from enum import Enum

from demo_opts import get_device

from constants import margin

class App:

    def __init__(self) -> None:
        self.state_changed = True
        self.route = "Intro"
        self.active_option = 0
        self.options = [
            "Calculator",
            "Calendar",
            "Turn off"
        ]
        self.main_menu_opts = [
            "Calculator",
            "Calendar",
            "Turn off"
        ]
        self.calculator_opts = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

    def on_key_press(self, key: KeyCode | Key | None) -> None:
        """Handle the key press for the main menu."""
        if key == Key.up and self.active_option > 0:
            self.state_changed = True
            self.active_option -= 1
        elif key == Key.down and self.active_option < len(self.options) - 1:
            self.state_changed = True
            self.active_option += 1
        elif key == Key.enter:
            self.state_changed = True
            if self.route == "Main menu":
                self.route = self.options[self.active_option]
                if self.route == "Calculator":
                    self.active_option = self.calculator_opts[0][0]
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

            if self.state_changed and self.route == "Intro":
                self.state_changed = False
                with canvas(device) as draw:
                    draw.text((0 + margin, 0 + margin),
                              "VOLKSMOBIEL", fill="white", font_size=9)
                    draw.text((0 + margin, 10 + margin),
                              "The phone for you", fill="white", font_size=9)

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
                              "> ", fill="white", font_size=9)
                    # draw.text((0 + margin, 10 + margin),
                    #           "1", fill="white", font_size=9)
                    # draw.text((10 + margin, 10 + margin),
                    #           "2", fill="white", font_size=9)
                    # draw.text((20 + margin, 10 + margin),
                    #           "3", fill="white", font_size=9)
                    # draw.text((0 + margin, 20 + margin),
                    #           "4", fill="white", font_size=9)
                    # draw.text((10 + margin, 20 + margin),
                    #           "5", fill="white", font_size=9)
                    # draw.text((20 + margin, 20 + margin),
                    #           "6", fill="white", font_size=9)
                    # draw.text((0 + margin, 30 + margin),
                    #           "7", fill="white", font_size=9)
                    # draw.text((10 + margin, 30 + margin),
                    #           "8", fill="white", font_size=9)
                    # draw.text((20 + margin, 30 + margin),
                    #           "9", fill="white", font_size=9)
                    

                    for idx, row in enumerate(self.options):
                        for jdx, option in enumerate(row):
                            draw.text((10 * jdx + margin, ((10 * (idx + 1)) + margin)),
                                    f"{option}", fill="white", font_size=9)
                            # if option == self.active_option:
                            #     draw.rectangle(
                            #         xy=(0, (10 * idx), device.width - margin,
                            #             (10 * idx) + 10 + 2 * margin),
                            #         outline="white"
                            #     )

            elif self.state_changed and self.route == "Exit":
                break



if __name__ == "__main__":
    device = get_device()
    app = App()
    app.main()
