from kivy.uix.button import Button
from abc import ABC, abstractmethod
from custom_exception import CustomException


class AbstractButton(ABC):
    def __init__(self, size=(0, 0), pos_hint=None):
        self.size = size
        self.pos_hint = pos_hint if pos_hint is not None else {}
        super().__init__()

    @abstractmethod
    def create_button(self):
        pass


class ButtonBuilder(AbstractButton):
    def __init__(self, text=None, image=None, on_release=None, *args, **kwargs):
        self.text = text
        self.image = image
        self.on_release = on_release
        super().__init__(*args, **kwargs)

    def create_button(self):
        if not self.text and not self.image:
            raise CustomException("Either text or image file path must be provided to create button.")
        btn = Button(text=self.text or "")
        if self.image:
            btn.background_normal = self.image
        btn.size = self.size
        btn.pos_hint = self.pos_hint
        if self.on_release:
            btn.bind(on_release=self.on_release)
        return btn

