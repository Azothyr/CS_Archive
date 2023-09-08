"""
Module that defines BarWidget, a BoxLayout with several buttons.
"""

from kivy.uix.boxlayout import BoxLayout
from abstract_button import ButtonBuilder


class BarWidget(BoxLayout):
    """
    A widget that contains a row of buttons for various game cus_funcs.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add buttons
        self.buttons = {
            "Explore": None,
            "Research": None,
            "Build": None
        }

        self.orientation = 'horizontal'
        self.size_hint = (1, 0.1)
        self.pos_hint = {'x': 0, 'y': 0}

        for button in self.buttons:
            btn = ButtonBuilder({
                'text': button,
                'size': (100, 50)
            }).create_button()
            self.add_widget(btn)
