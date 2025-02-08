from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def log(self, message):
        pass

class debug_logger(Base):
    def log(self, message):
        print(f'DEBUG: {message}')

class info_logger(Base):
    def log(self, message):
        print(f'INFO: {message}')

class error_logger(Base):
    def log(self, message):
        print(f'ERROR: {message}')