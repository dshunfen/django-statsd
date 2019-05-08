from __future__ import absolute_import
import django_cloudwatch

try:
    import redis

    class CloudwatchRedis(redis.Redis):

        def execute_command(self, func_name, *args, **kwargs):
            with django_cloudwatch.with_('redis.%s' % func_name.lower()):
                return origRedis.execute_command(self, func_name, *args,
                                                 **kwargs)

    origRedis = None
    # NOTE issubclass is true if both are the same class
    if not issubclass(redis.Redis, CloudwatchRedis):
        origRedis = redis.Redis
        redis.Redis = CloudwatchRedis
except ImportError:
    pass
