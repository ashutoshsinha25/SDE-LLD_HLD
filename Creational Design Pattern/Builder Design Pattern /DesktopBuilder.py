from abc import ABC, abstractmethod
from Desktop import Desktop, SonyDesktop, HPDesktop, DellDesktop


class DesktopBuilder(ABC):
    def __init__(self):
        self.desktop = None

    @abstractmethod
    def processor(self):
        pass

    @abstractmethod
    def ram(self):
        pass

    @abstractmethod
    def storage(self):
        pass

    @abstractmethod
    def graphics(self):
        pass

    @abstractmethod
    def os(self):
        pass

    @abstractmethod
    def getDesktop(self):
        pass
    
    @abstractmethod
    def display(self):
        pass 



    

class DellDesktopBuilder(DesktopBuilder):
    def __init__(self):
        self.desktop = DellDesktop()  

    def processor(self):
        self.desktop.processor()

    def ram(self):
        self.desktop.ram()

    def storage(self):
        self.desktop.storage()

    def graphics(self):
        self.desktop.graphics()

    def os(self):
        self.desktop.os()

    def getDesktop(self):
        return self.desktop  

    def display(self):
        self.desktop.display()




    
class SonyDesktopBuilder(DesktopBuilder):
    def __init__(self):
        self.desktop = SonyDesktop()  

    def processor(self):
        self.desktop.processor()

    def ram(self):
        self.desktop.ram()

    def storage(self):
        self.desktop.storage()

    def graphics(self):
        self.desktop.graphics()

    def os(self):
        self.desktop.os()

    def getDesktop(self):
        return self.desktop

    def display(self):
        self.desktop.display()

    
class HPDesktopBuilder(DesktopBuilder):
    def __init__(self):
        self.desktop = HPDesktop()  

    def processor(self):
        self.desktop.processor()

    def ram(self):
        self.desktop.ram()

    def storage(self):
        self.desktop.storage()

    def graphics(self):
        self.desktop.graphics()

    def os(self):
        self.desktop.os()

    def getDesktop(self):
        return self.desktop

    def display(self):
        self.desktop.display()



    


