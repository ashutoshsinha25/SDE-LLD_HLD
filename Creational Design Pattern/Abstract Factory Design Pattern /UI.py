from abc import ABC, abstractmethod 


class IButton(ABC):
    @abstractmethod
    def press(self):
        pass 

class ITextbox(ABC):
    @abstractmethod
    def press(self):
        pass 


class WinButton(IButton):
    def press(self):
        print('Win Button pressed')

class WinTextbox(ITextbox):
    def press(self):
        print('Win Textbox pressed')


class MacButton(IButton):
    def press(self):
        print('Mac Button pressed') 

class MacTextbox(ITextbox): 
    def press(self):
        print('Mac Textbox pressed')    

