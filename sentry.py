import sentry_sdk

sentry_sdk.init(
    dsn="https://9e3db0e9c29408a0a8f7a48eac61a59e@o4507788027297792.ingest.us.sentry.io/4507790466023424",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for tracing.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

division_by_zero = 1 / 0