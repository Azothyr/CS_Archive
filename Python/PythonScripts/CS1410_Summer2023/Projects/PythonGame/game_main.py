from kivy.uix.screenmanager import ScreenManager
from main_menu_screens import *


class BlacksmithGame(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(OptionScreen(name='options'))
        return sm


if __name__ == "__main__":
    BlacksmithGame().run()
