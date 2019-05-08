from __future__ import with_statement
import django_cloudwatch


class TimingCursorWrapper(object):

    def execute(self, *args, **kwargs):
        with django_cloudwatch.with_('sql.%s' % self.db.alias):
            return self.cursor.execute(*args, **kwargs)

    def executemany(self, *args, **kwargs):
        with django_cloudwatch.with_('sql.%s' % self.db.alias):
            return self.cursor.executemany(*args, **kwargs)
