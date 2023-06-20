from kivy.app import App
from kivy.clock import Clock
from kivy.uix.spinner import Spinner
from base_screen import BaseScreen
from abstract_button import ButtonBuilder


class MainMenuScreen(BaseScreen):
    """Main Menu Screen"""

    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)

        # Creating a Play Game button
        play_btn = ButtonBuilder(text='Play', size=(100, 50),
                                 pos_hint={'x': 0.5, 'y': 0.5}, on_release=self.go_to_play).create_button()

        # Creating a Game options button
        options_btn = ButtonBuilder(text='Options', size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5},
                                    on_release=self.go_to_options).create_button()

        # Creating a Quit button
        quit_btn = ButtonBuilder(text='Quit', size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5},
                                 on_release=App.get_running_app().stop).create_button()

        # Add buttons to the button_layout
        self.button_layout.add_widget(play_btn)
        self.button_layout.add_widget(options_btn)
        self.button_layout.add_widget(quit_btn)

    def go_to_play(self, instance):
        self.manager.current = 'play'

    def go_to_options(self, instance):
        self.manager.current = 'options'


class OptionScreen(BaseScreen):
    """Game Options/Settings Screen"""

    def __init__(self, **kwargs):
        super(OptionScreen, self).__init__(**kwargs)

        self.spinner = Spinner(text='Select screen size', pos_hint={'x': 0.5, 'y': 0.5},
                               values=('Fullscreen', '1920x1080', '1280x1024', '1024x768', '800x600'))

        apply_btn = ButtonBuilder(text='Apply', size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5},
                                  on_release=self.apply_changes).create_button()

        back_btn = ButtonBuilder(text='Back', size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5},
                                 on_release=self.go_back).create_button()

        self.button_layout.add_widget(self.spinner)
        self.button_layout.add_widget(apply_btn)
        self.button_layout.add_widget(back_btn)

    def apply_changes(self, instance):
        if self.spinner.text == 'Fullscreen':
            Clock.schedule_once(lambda dt: App.get_running_app().root_window.maximize(), 0)
        elif 'x' in self.spinner.text:
            width, height = map(int, self.spinner.text.split('x'))
            Clock.schedule_once(lambda dt: self.change_screen_size(width, height), 0)
        else:
            print("Invalid screen size selected.")

    def go_back(self, instance):
        self.manager.current = 'menu'

    @staticmethod
    def change_screen_size(width, height):
        App.get_running_app().root_window.size = (width, height)
