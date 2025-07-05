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
# Sony Desktop - CPU: AMD Ryzen 7, RAM: 32GB, Storage: 2TB SSD, GPU: AMD Radeon RX 6700XT, OS: Windows 11
# HP Desktop - CPU: Intel i5, RAM: 8GB, Storage: 1TB HDD, GPU: Intel Integrated Graphics, OS: Windows 10
