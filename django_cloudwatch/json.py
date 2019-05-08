from __future__ import absolute_import
import django_cloudwatch

try:
    import json

    if not hasattr(json, 'cloudwatch_patched'):
        json.cloudwatch_patched = True
        json.load = django_cloudwatch.wrapper('json', json.load)
        json.loads = django_cloudwatch.wrapper('json', json.loads)
        json.dump = django_cloudwatch.wrapper('json', json.dump)
        json.dumps = django_cloudwatch.wrapper('json', json.dumps)
except ImportError:
    pass

try:
    import cjson

    if not hasattr(json, 'cloudwatch_patched'):
        cjson.cloudwatch_patched = True
        cjson.encode = django_cloudwatch.wrapper('cjson', cjson.encode)
        cjson.decode = django_cloudwatch.wrapper('cjson', cjson.decode)
except ImportError:
    pass
