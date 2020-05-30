import logging

logging.basicConfig(filename="validation_logs.log", level=logging.DEBUG, format='%(levelname)s %(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()

logger.debug("This is debug level")
logger.info("This is info level")
logger.error("This is error level")
logger.critical("This is critical level")
logger.warning("This is warning level")
