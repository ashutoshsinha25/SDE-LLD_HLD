from abc import ABC, abstractmethod

class ILogger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class debug_logger(ILogger):
    def log(self, message):
        print(f'DEBUG: {message}')

class info_logger(ILogger):
    def log(self, message):
        print(f'INFO: {message}')

class error_logger(ILogger):
    def log(self, message):
        print(f'ERROR: {message}')

