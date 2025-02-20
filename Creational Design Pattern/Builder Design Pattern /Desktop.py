from abc import ABC, abstractmethod

class Desktop(ABC):
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
    def __str__(self):
        pass

    @abstractmethod
    def display(self):
        pass 


class SonyDesktop(Desktop):
    def processor(self):
        return "AMD Ryzen 7"

    def ram(self):
        return "32GB"

    def storage(self):
        return "2TB SSD"

    def graphics(self):
        return "AMD Radeon RX 6700XT"

    def os(self):
        return "Windows 11"

    def __str__(self):
        return f"Sony Desktop - CPU: {self.processor()}, RAM: {self.ram()}, Storage: {self.storage()}, GPU: {self.graphics()}, OS: {self.os()}"

    def display(self):
        print(self)


class HPDesktop(Desktop):
    def processor(self):
        return "Intel i5"

    def ram(self):
        return "8GB"

    def storage(self):
        return "512GB SSD"

    def graphics(self):
        return "Integrated Intel Graphics"

    def os(self):
        return "Windows 10"

    def __str__(self):
        return f"HP Desktop - CPU: {self.processor()}, RAM: {self.ram()}, Storage: {self.storage()}, GPU: {self.graphics()}, OS: {self.os()}"

    def display(self):
        print(self)


class DellDesktop(Desktop):
    def processor(self):
        return "Intel i7"

    def ram(self):
        return "16GB"

    def storage(self):
        return "1TB SSD"

    def graphics(self):
        return "NVIDIA RTX 3060"

    def os(self):
        return "Windows 11"

    def __str__(self):
        return f"Dell Desktop - CPU: {self.processor()}, RAM: {self.ram()}, Storage: {self.storage()}, GPU: {self.graphics()}, OS: {self.os()}"

    def display(self):
        print(self)
