from kivy.uix.boxlayout import BoxLayout
from abstract_button import ButtonBuilder


class BarWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(BarWidget, self).__init__(**kwargs)

        # Add buttons
        self.buttons = {
            "Explore": None,
            "Research": None,
            "Build": None
        }

        self.orientation = 'horizontal'
        self.size_hint = (1, 0.1)
        self.pos_hint = {'x': 0, 'y': 0}

        for button in self.buttons.keys():
            btn = ButtonBuilder(text=button, size=(100, 50)).create_button()
            self.add_widget(btn)
