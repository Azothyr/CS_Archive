"""
This module contains the main application for the Blacksmith Game.
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from screens import MainMenuScreen, OptionScreen, PlayScreen


class BlacksmithGame(App):
    """
    Main application class for the Blacksmith Game.
    """

    def build(self):
        """
        Build and return the root widget for the Blacksmith Game.
        """
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainMenuScreen(name='main'))
        screen_manager.add_widget(OptionScreen(name='options'))
        screen_manager.add_widget(PlayScreen(name='play'))
        return screen_manager


if __name__ == "__main__":
    BlacksmithGame().run()
