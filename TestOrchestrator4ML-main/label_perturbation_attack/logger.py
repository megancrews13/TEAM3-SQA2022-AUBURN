import logging

def getLoggerObj():
    logging.basicConfig(filename="log.LOG", level=logging.INFO, format='%(asctime)s:::%(name)s:::%(levelname)s:::%(message)s', datefmt='%d-%b-%y %H:%M:%S')
    loggerObj = logging.getLogger('logger')
    return loggerObj