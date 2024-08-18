import os
from dotenv import load_dotenv
import sentry_sdk
import logging
from sentry_sdk.integrations.logging import LoggingIntegration
load_dotenv()

sentry_logging = LoggingIntegration(
    level=logging.INFO,
    event_level=logging.ERROR
)
sentry_sdk.init(
    dsn=os.getenv('DNS_SENTRY'),
    integrations=[sentry_logging]
)