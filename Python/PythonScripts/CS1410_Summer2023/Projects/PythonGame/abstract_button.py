"""
This module provides an AbstractButton class and a ButtonBuilder class for creating buttons.
"""

from abc import ABC, abstractmethod
from kivy.uix.button import Button
from custom_exception import CustomException


class AbstractButton(ABC):
    """
    This class provides an interface for creating buttons.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, size=(0, 0), pos_hint=None):
        self.size = size
        self.pos_hint = pos_hint if pos_hint is not None else {}

    @abstractmethod
    def create_button(self):
        """
        Abstract method for creating a button.
        """


class ButtonBuilder(AbstractButton):
    """
    This class provides a concrete implementation of AbstractButton for creating buttons.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, params):
        size = params.get('size', (0, 0))
        pos_hint = params.get('pos_hint', None)
        super().__init__(size, pos_hint)
        self.text = params.get('text', None)
        self.image = params.get('image', None)
        self.on_release = params.get('on_release', None)

    def create_button(self):
        """
        Create a button with the given parameters.
        If no text or image is provided, a CustomException is raised.
        """
        if not self.text and not self.image:
            raise CustomException(
                "Either text or image file path must be provided to create button.")
        btn = Button(text=self.text or "")
        if self.image:
            btn.background_normal = self.image
        btn.size = self.size
        btn.pos_hint = self.pos_hint
        if self.on_release:
            # pylint: disable=no-member
            btn.bind(on_release=self.on_release)
        return btn
