from django.core import exceptions
from django.conf import settings


def get_setting(key, default=None):
    try:
        value = getattr(settings, key, default)
    except exceptions.ImproperlyConfigured:
        value = default

    return value


#: Enable tracking all requests using the middleware
CLOUDWATCH_TRACK_MIDDLEWARE = get_setting('CLOUDWATCH_TRACK_MIDDLEWARE', False)

#: Set the global cloudwatch prefix if needed. Otherwise use the root
CLOUDWATCH_PREFIX = get_setting('CLOUDWATCH_PREFIX')

#: Enable warnings such as timers which are started but not finished. Defaults
#: to DEBUG if not configured
CLOUDWATCH_DEBUG = get_setting('CLOUDWATCH_DEBUG', get_setting('DEBUG'))

#: Enable creating tags as well as the bare version. This causes an ajax view
#: to be stored both as the regular view name and as the ajax tag. Supported
#: separators are _is_ and =
CLOUDWATCH_TAGS_LIKE = get_setting('CLOUDWATCH_TAGS_LIKE')

#: Cloudwatch host, defaults to 127.0.0.1
CLOUDWATCH_HOST = get_setting('CLOUDWATCH_HOST', '127.0.0.1')

#: Cloudwatch port, defaults to 8125
CLOUDWATCH_PORT = get_setting('CLOUDWATCH_PORT', 8125)

#: Cloudwatch sample rate, lowering this decreases the (random) odds of actually
#: submitting the data. Between 0 and 1 where 1 means always
CLOUDWATCH_SAMPLE_RATE = get_setting('CLOUDWATCH_SAMPLE_RATE', 1.0)


