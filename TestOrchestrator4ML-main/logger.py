import logging

def getLoggerObj():
    logging.basicConfig(filename="log.LOG", filemode='w', format='%(asctime)s:::%(name)s:::%(levelname)s:::%(message)s', datefmt='%d-%b-%y %H:%M:%S')
    loggerObj = logging.getLogger('gen-logger')
    return loggerObj