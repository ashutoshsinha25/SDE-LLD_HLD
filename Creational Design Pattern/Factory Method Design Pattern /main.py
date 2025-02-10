from LoggerFactory import  InfoLoggerFactory, ErrorLoggerFactory, DebugLoggerFactory 

info_logger_factory = InfoLoggerFactory()
error_logger_factory = ErrorLoggerFactory()
debug_logger_factory = DebugLoggerFactory()

info_logger = info_logger_factory.create_logger()
error_logger = error_logger_factory.create_logger()
debug_logger = debug_logger_factory.create_logger()

info_logger.log('This is an info message')
error_logger.log('This is an error message')
debug_logger.log('This is a debug message')


# Output
# INFO: This is an info message
# ERROR: This is an error message
# DEBUG: This is a debug message
