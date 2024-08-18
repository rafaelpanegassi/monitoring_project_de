import logging
from logging import INFO, DEBUG, ERROR, CRITICAL, WARNING, basicConfig
from logging import FileHandler, StreamHandler

basicConfig(
    level=DEBUG,
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[FileHandler('logging.txt', 'a'), StreamHandler()]
)

logging.debug('Aviso de Debug')
logging.info('Aviso de Informacao')
logging.warning('Aviso de Warning')
logging.error('Aviso de Error')
logging.critical('Aviso de Critical')
