from kivy.uix.button import Button
from abc import ABC, abstractmethod
from custom_exception import CustomException


class AbstractButton(ABC):
    def __init__(self, size=(0, 0), pos_hint=None, action=None):
        self.size = size
        self.pos_hint = pos_hint if pos_hint is not None else {}
        self.action = action
        super().__init__()

    @abstractmethod
    def create_button(self):
        pass


class ButtonBuilder(AbstractButton):
    def __init__(self, *args, **kwargs):
        self.text = None
        self.image = None
        super().__init__(*args, **kwargs)

    def create_button(self):
        if not self.text or not self.image:
            raise CustomException("Text or image file path must be provided to create button.")
        btn = Button(text=self.text, background_normal=self.image, size=self.size, pos_hint=self.pos_hint)
        if self.action:
            btn.bind(on_release=self.action)
