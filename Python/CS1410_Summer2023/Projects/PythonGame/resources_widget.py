"""
Module for defining the ResourcesWidget which displays the game resources.
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class ResourcesWidget(BoxLayout):
    """
    A widget that displays the game resources and their current quantities.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Add resources
        self.resources = {
            "Gold": 0,
            "Iron Ore": 0,
            "Wood": 0,
            "Researchers": 0,
            "Workers": 0
        }

        self.orientation = 'vertical'
        self.size_hint = (0.2, 0.2)
        self.pos_hint = {'x': 0, 'y': 0.8}

        for resource, amount in self.resources.items():
            self.add_widget(Label(text=f"{resource}: {amount}"))
