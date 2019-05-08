import cloudwatch
from . import settings


def get_connection(host=None, port=None, sample_rate=None):
    if not host:
        host = settings.CLOUDWATCH_HOST

    if not port:
        port = settings.CLOUDWATCH_PORT

    if not sample_rate:
        sample_rate = settings.CLOUDWATCH_SAMPLE_RATE

    return cloudwatch.Connection(host, port, sample_rate)


def get_client(name, connection=None, class_=cloudwatch.Client):
    if not connection:
        connection = get_connection()

    return class_(name, connection)


def get_timer(name, connection=None):
    return get_client(name, connection, cloudwatch.Timer)


def get_counter(name, connection=None):
    return get_client(name, connection, cloudwatch.Counter)
