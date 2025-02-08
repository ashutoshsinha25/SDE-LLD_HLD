from Logger import debug_logger, error_logger, info_logger

class LoggerFactory:
    def create_logger(self, loglevel):
        if loglevel == 'info':
            return info_logger()
        elif loglevel == 'error':
            return error_logger()
        else:
            return debug_logger()
