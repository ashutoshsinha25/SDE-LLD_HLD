from Loggerfactory import LoggerFactory

logger_factory = LoggerFactory()
logger = logger_factory.create_logger('info')
logger.log('This is an info message')

logger = logger_factory.create_logger('error')
logger.log('This is an error message')

logger = logger_factory.create_logger('debug')
logger.log('This is a debug message')

# Output
# INFO: This is an info message
# ERROR: This is an error message
# DEBUG: This is a debug message