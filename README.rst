Introduction
============

`django_cloudwatch` is a middleware that uses `python-cloudwatch` to log query
and view durations to AWS cloudwatch.

* Documentation
    - http://django-stats.readthedocs.org/en/latest/
* Source
    - https://github.com/dshunfen/django-cloudwatch
* Bug reports 
    - https://github.com/dshunfenthal/django-cloudwatch/issues
* Package homepage
    - https://pypi.python.org/pypi/django-cloudwatch
* Python Cloudwatch
    - https://github.com/WoLpH/python-cloudwatch
* Graphite
    - http://graphite.wikidot.com
* Cloudwatch
    - code: https://github.com/etsy/cloudwatch
    - blog post: http://codeascraft.etsy.com/2011/02/15/measure-anything-measure-everything/


Install
=======

To install simply execute `python setup.py install`.
If you want to run the tests first, run `python setup.py test`


Usage
=====

To install, add the following to your ``settings.py``:

1. ``django_cloudwatch`` to the ``INSTALLED_APPS`` setting.
2. ``django_cloudwatch.middleware.CloudwatchMiddleware`` to the **top** of your
    ``MIDDLEWARE_CLASSES``
3. ``django_cloudwatch.middleware.CloudwatchMiddlewareTimer`` to the **bottom** of your
    ``MIDDLEWARE_CLASSES``

Advanced Usage
--------------

    >>> def some_view(request):
    ...     with request.timings('something_to_time'):
    ...         # do something here
    ...         pass
    >>>    
    >>> def some_view(request):
    ...     request.timings.start('something_to_time')
    ...     # do something here
    ...     request.timings.stop('something_to_time')

