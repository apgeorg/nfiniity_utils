import threading
import time


class Timer(object):

    def __init__(self, interval, callback_func, oneshot=False, args=None, kwargs=None):
        self._interval = interval
        self._oneshot = oneshot
        self._f = callback_func
        self._args = args if args is not None else []
        self._kwargs = kwargs if kwargs is not None else {}
        self._timer = None
        self._start_time = None
        self._elapsed_time = None
        self._remaining_time = None

    def _callback(self):
        self._f(*self._args, **self._kwargs)
        if not self._oneshot:
            self.start()
        else:
            self.stop()

    def stop(self):
        if self._timer:
            self._timer.cancel()
            self._elapsed_time = time.time() - self._start_time
            self._remaining_time = self._interval - self._elapsed_time
            self._timer = None

    def start(self, interval=None):
        self._interval = interval if interval is not None else self._interval
        self._timer = threading.Timer(self._interval, self._callback)
        self._start_time = time.time()
        self._timer.start()

    @property
    def elapsed(self):
        return self._elapsed_time

    @property
    def remaining(self):
        return self._remaining_time

    @property
    def running(self):
        return True if self._timer else False
