"""
This module contains classes for the various screens used in the app.
"""
# pylint: disable=W0511
from kivy.app import App
from kivy.uix.spinner import Spinner
from base_screen import BaseScreen
from resources_widget import ResourcesWidget
from bar_widget import BarWidget
from abstract_button import ButtonBuilder


class MainMenuScreen(BaseScreen):
    """
    This class represents the Main Menu Screen.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Creating a Play Game button
        play_btn = ButtonBuilder({
            'text': 'Play',
            'size': (100, 50),
            'pos_hint': {'x': 0.5, 'y': 0.5},
            'on_release': self.go_to_play
        }).create_button()

        # Creating a Game options button
        options_btn = ButtonBuilder({
            'text': 'Options',
            'size': (100, 50),
            'pos_hint': {'x': 0.5, 'y': 0.5},
            'on_release': self.go_to_options
        }).create_button()

        # Creating a Quit button
        quit_btn = ButtonBuilder({
            'text': 'Quit',
            'size': (100, 50),
            'pos_hint': {'x': 0.5, 'y': 0.5},
            'on_release': App.get_running_app().stop
        }).create_button()

        # Add buttons to the button_layout
        self.button_layout.add_widget(play_btn)
        self.button_layout.add_widget(options_btn)
        self.button_layout.add_widget(quit_btn)

    def go_to_play(self, _instance):
        """Change current screen to play screen."""
        self.manager.current = 'play'

    def go_to_options(self, _instance):
        """Change current screen to options screen."""
        self.manager.current = 'options'


class OptionScreen(BaseScreen):
    """This class represents the Game Options/Settings Screen."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.spinner = Spinner(
            text='Select screen size',
            pos_hint={'x': 0.5, 'y': 0.5},
            values=('Fullscreen', '1920x1080', '1280x1024', '1024x768', '800x600')
        )

        apply_btn = ButtonBuilder({
            'text': 'Apply *Broken*',
            'size': (100, 50),
            'pos_hint': {'x': 0.5, 'y': 0.5},
            'on_release': self.apply_changes
        }).create_button()

        back_btn = ButtonBuilder({
            'text': 'Back',
            'size': (100, 50),
            'pos_hint': {'x': 0.5, 'y': 0.5},
            'on_release': self.go_back
        }).create_button()

        self.button_layout.add_widget(self.spinner)
        self.button_layout.add_widget(apply_btn)
        self.button_layout.add_widget(back_btn)

    def apply_changes(self, _instance):
        """
        Apply the changes based on the selected options.
        Currently, a placeholder and does not change screen size.
        Previous implementation caused a fatal system error
        """
        selected_option = self.spinner.text
        print(f"Selected option: {selected_option}")
        # TODO: Implement the functionality to change screen size based on the selected option

    def go_back(self, _instance):
        """
        Go back to the main menu screen.
        """
        self.manager.current = 'main'


class PlayScreen(BaseScreen):
    """
    This class represents the actual Play Screen where the game occurs.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        resources = ResourcesWidget(size_hint=(1, None), height=50)
        self.add_widget(resources)

        game_bar = BarWidget()
        self.add_widget(game_bar)

        back_btn = ButtonBuilder({
            'text': 'Back',
            'size': (100, 50),
            'pos_hint': {'x': 0.9, 'y': 0.9},
            'on_release': self.go_back
        }).create_button()

        self.button_layout.add_widget(back_btn)

    def go_back(self, _instance):
        """
        Go back to the main menu screen.
        """
        self.manager.current = 'main'
