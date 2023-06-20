from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from game_scenes import *


class BlacksmithGame(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(OptionScreen(name='options'))
        return sm


if __name__ == "__main__":
    BlacksmithGame().run()
