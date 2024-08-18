from logging import DEBUG, INFO, WARNING, ERROR, CRITICAL
from loguru import logger
from sentry_sdk import init
from sentry_sdk.integrations.logging import LoggingIntegration, EventHandler
import os
from dotenv import load_dotenv
load_dotenv()


init(
   dsn=os.getenv('DNS_SENTRY'),
    integrations=[LoggingIntegration(level=None, event_level=None)]
)  # Inicia o sentry

logger.add(
    EventHandler(level=WARNING), format="{time} {level} {message}",
)  # Adiciona o sentry ao loguru

# Logando
logger.debug("A")
logger.info("b")
logger.error("C", extra=dict(bar=43))
logger.exception("d")