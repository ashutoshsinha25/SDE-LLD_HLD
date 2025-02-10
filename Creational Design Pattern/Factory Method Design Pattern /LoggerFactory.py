from Logger import info_logger, debug_logger, error_logger
from abc import ABC, abstractmethod

class ILoggerFactory(ABC):
    @abstractmethod
    def create_logger(self, message):
        pass

class InfoLoggerFactory(ILoggerFactory):
    def create_logger(self):
        return info_logger()
    
class DebugLoggerFactory(ILoggerFactory):
    def create_logger(self):
        return debug_logger()
    
class ErrorLoggerFactory(ILoggerFactory):
    def create_logger(self):
        return error_logger()
