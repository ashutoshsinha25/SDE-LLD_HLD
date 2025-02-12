from UI import WinButton, WinTextbox, MacButton, MacTextbox
from abc import ABC, abstractmethod

class IUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_textbox(self):
        pass


class WinUIFactory(IUIFactory):
    def create_button(self):
        return WinButton()

    def create_textbox(self):
        return WinTextbox()
    
class MacUIFactory(IUIFactory):
    def create_button(self):
        return MacButton()

    def create_textbox(self):
        return MacTextbox()
