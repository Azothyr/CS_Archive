from kivy.uix.screenmanager import Screen
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class BaseScreen(Screen):
    def __init__(self, **kwargs):
        super(BaseScreen, self).__init__(**kwargs)

        # set full screen
        Window.fullscreen = 'auto'

        # Create a layout
        self.layout = RelativeLayout()

        # Create an image
        background_img = Image(source='resources/images/WarBackgroundTest.jpg')
        background_img.allow_data_stretch = True
        background_img.keep_data_ratio = False  # Set this to True if you want to keep the aspect ratio
        self.float_layout = FloatLayout(size_hint=(1, 1))
        self.float_layout.add_widget(background_img)

        # Create a vertical BoxLayout for the buttons
        self.button_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(100, 150),
                                       pos_hint={'center_x': 0.5, 'y': 0})

        # Add widgets to the layout
        self.layout.add_widget(self.float_layout)
        self.layout.add_widget(self.button_layout)

        # Add the layout to the screen
        self.add_widget(self.layout)
