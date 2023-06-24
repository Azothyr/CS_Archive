from kivy.uix.screenmanager import ScreenManager
from screens import *


class BlacksmithGame(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(OptionScreen(name='options'))
        sm.add_widget(PlayScreen(name='play'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


if __name__ == "__main__":
    BlacksmithGame().run()
