import sentry_sdk
import os
from dotenv import load_dotenv
load_dotenv()

sentry_sdk.init(
    dsn=os.getenv('DNS_SENTRY'),
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


division_by_zero = 1 / 0


