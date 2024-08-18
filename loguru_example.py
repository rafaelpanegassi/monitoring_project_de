from sys import stderr
from loguru import logger

logger.remove()

logger.add(
    sink='loguru.txt', 
    format='{file} {time} {level} {line}', 
    filter=lambda rec: 'senha' not in rec['message'].lower(), 
    level='WARNING'
)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('senha')
