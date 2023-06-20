from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core import window
from abstract_button import ButtonBuilder


class MainMenuScreen(Screen):
    """Main Menu Screen"""
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        # Pass the app instance to MainMenu
        self.app = None

        # set full screen
        window.Window.fullscreen = 'auto'

        # Create a layout
        layout = RelativeLayout()

        # Create an image
        background_img = Image(source='resources/images/WarBackgroundTest.jpg')
        background_img.allow_data_stretch = True
        background_img.keep_data_ratio = False  # Set this to True if you want to keep the aspect ratio
        float_layout = FloatLayout(size_hint=(1, 1))
        float_layout.add_widget(background_img)

        # Create a vertical BoxLayout for the buttons
        button_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150),
                                  pos_hint={'center_x': 0.5, 'y': 0})

        # Creating a Play Game button
        play_btn = ButtonBuilder(text='Options', size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5},
                                 on_release=self.go_to_play).create_button()

        # Creating a Game options button
        options_btn = ButtonBuilder(text='Options', size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5},
                                    on_release=self.go_to_options).create_button()

        # Creating a Quit button
        quit_btn = ButtonBuilder(text='Options', size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5},
                                 on_release=self.app.stop).create_button()

        # Add buttons to the button_layout
        button_layout.add_widget(play_btn)
        button_layout.add_widget(options_btn)
        button_layout.add_widget(quit_btn)

        # Add widgets to the layout
        layout.add_widget(float_layout)
        layout.add_widget(button_layout)

    def go_to_play(self, instance):
        self.manager.current = 'options'

    def go_to_options(self, instance):
        self.manager.current = 'options'


class OptionScreen(Screen):
    """Game Options/Settings Screen"""
    def __init__(self, **kwargs):
        super(OptionScreen, self).__init__(**kwargs)
        box = BoxLayout(orientation='vertical')

        self.spinner = Spinner(text='Select screen size',
                               values=('Fullscreen', '1920x1080', '1280x1024', '1024x768', '800x600'))

        apply_btn = ButtonBuilder(text='Apply', size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5},
                                  on_release=self.apply_changes).create_button()

        back_btn = ButtonBuilder(text='Back', size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5},
                                 on_release=self.go_back).create_button()

        box.add_widget(self.spinner)
        box.add_widget(apply_btn)
        box.add_widget(back_btn)

        self.add_widget(box)

    def apply_changes(self, instance):
        if self.spinner.text == 'Fullscreen':
            App.get_running_app().root_window.maximize()
        else:
            width, height = map(int, self.spinner.text.split('x'))
            App.get_running_app().root_window.size = (width, height)

    def go_back(self, instance):
        self.manager.current = 'menu'
