from pynput.keyboard import Listener, KeyCode, Key
from luma.core.render import canvas

from demo_opts import get_device

import env
import utils

from apps.routes import Routes
from apps.intro import Intro
from apps.main_menu import MainMenu
from apps.calculator import Calculator
from apps.sms import Sms

class App:

    def __init__(self) -> None:
        self.state_changed = True
        self.route = Routes().intro
        self.prev_route = self.route
        self.active_option = 0
        self.options = Intro().options
        self.flat_options = self.options


    # DEVELOPMENT ONLY
    def on_key_press(self, key: KeyCode | Key | None) -> None:
        """Handle the key press for the main menu."""
        if key not in [Key.up, Key.down, Key.enter, Key.esc]:
            return
        
        # State is valid, changed
        self.state_changed = True

        # Create a 1d array of options
        self.flat_options = utils.flatten_2d_list(self.options)

        if key == Key.up and self.active_option > 0:
            self.active_option -= 1
            return

        if key == Key.down and self.active_option < len(self.flat_options) - 1:
            self.active_option += 1
            return
        
        if key == Key.esc:
            self.route = Routes().turn_off
            return
        
        args = dict(
            app=self,
            key=key,
            route=self.route,
            active_option=self.active_option
        )

        # Define route actions
        Intro().action(**args)

        # if key == Key.enter and self.flat_options[self.active_option] == constants.back_option:
            
        #     return

        # if back_selected:

        #     if is_back and self.route == Routes().main_menu:
        #         self.active_option = 0
        #         self.options = MainMenu().options

        #     if not is_back:
        #         if self.route == Routes().main_menu:
        #             self.route = self.options[self.active_option]
        #             self.prev_route = Routes().main_menu
        #             if self.route == Routes().sms:
        #                 self.active_option = 0
        #                 self.options = Sms().options
        #             if self.route == Routes().calculator:
        #                 self.active_option = 0
        #                 self.options = Calculator().options


    def loop_fn(self):
        """Method for registering apps"""
        args = dict(
            route=self.route,
            canvas=canvas,
            device=device,
            active_option=self.active_option,
        )

        # Define routes display
        Intro().show(**args)
        MainMenu().show(**args)
        Calculator().show(**args)
        Sms().show(**args)


    def main(self) -> None:
        """Main UI Loop"""

        if env.DEBUG:
            listener = Listener(self.on_key_press)
            listener.start()


        while True:
            if self.state_changed:
                self.state_changed = False
                self.loop_fn()

                if self.route == Routes().turn_off:
                    break


if __name__ == "__main__":
    device = get_device()
    app = App()
    app.main()
