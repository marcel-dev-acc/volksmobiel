import time
from pynput.keyboard import Listener, KeyCode, Key
from luma.core.render import canvas

from demo_opts import get_device

from constants import margin

class App:

    def __init__(self) -> None:
        self.state_changed = True
        self.route = "intro"
        self.active_option = 0
        self.options = [
            "Calculator",
            "Calendar",
            "Turn off"
        ]

    def on_key_press(self, key: KeyCode | Key | None) -> None:
        """Handle the key press for the main menu"""
        if key == Key.up and self.active_option > 0:
            self.state_changed = True
            self.active_option -= 1
        elif key == Key.down and self.active_option < len(self.options) - 1:
            self.state_changed = True
            self.active_option += 1
        elif key == Key.enter:
            self.state_changed = True
            print('ENTER')
            self.route = "main_menu"

    def main(self):

        listener = Listener(self.on_key_press)
        listener.start()

        while True:

            if self.state_changed and self.route == "intro":
                self.state_changed = False
                with canvas(device) as draw:
                    draw.text((0 + margin, 0 + margin), "VOLKSMOBIEL", fill="white", font_size=9)
                    draw.text((0 + margin, 10 + margin), "The phone for you", fill="white", font_size=9)
            
            elif self.state_changed and self.route == "main_menu":
                self.state_changed = False
                with canvas(device) as draw:
                    for idx, option in enumerate(self.options):
                        draw.text((0 + margin, ((10 * idx) + margin)), f"{idx + 1}: {option}", fill="white", font_size=9)
                        if idx == self.active_option:
                            draw.rectangle(
                                xy=(0, (10 * idx), device.width - margin, (10 * idx) + 10 + 2 * margin),
                                outline="white"
                            )

            time.sleep(0.1)

if __name__ == "__main__":
    device = get_device()
    app = App()
    app.main()