from DesktopBuilder import SonyDesktopBuilder, HPDesktopBuilder

class DesktopDirector:
    def __init__(self, desktopBuilder):
        self.desktopBuilder = desktopBuilder

    def buildDesktop(self):
        self.desktopBuilder.processor()
        self.desktopBuilder.ram()
        self.desktopBuilder.storage()
        self.desktopBuilder.graphics()
        self.desktopBuilder.os()

    def getDesktop(self):
        return self.desktopBuilder.getDesktop()


if __name__ == '__main__':
    sonyDesktopBuilder = SonyDesktopBuilder()
    hpDesktopBuilder = HPDesktopBuilder()

    desktopDirector = DesktopDirector(sonyDesktopBuilder)
    desktopDirector.buildDesktop()
    desktop = desktopDirector.getDesktop()
    desktop.display()

    desktopDirector = DesktopDirector(hpDesktopBuilder)
    desktopDirector.buildDesktop()
    desktop = desktopDirector.getDesktop()
    desktop.display()

# Output
# Sony Desktop
# HP Desktop
