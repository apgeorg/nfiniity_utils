import threading
import time


class Timer(object):

    def __init__(self, interval, callback_func, oneshot=False, args=[], kwargs={}):
        self._interval = interval
        self._oneshot = oneshot
        self._f = callback_func
        self._args = args
        self._kwargs = kwargs
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
        if self.running():
            self._timer.cancel()
            self._elapsed_time = time.time() - self._start_time
            self._remaining_time = self._interval - self._elapsed_time
            self._timer = None

    def start(self):
        self._timer = threading.Timer(self._interval, self._callback)
        self._start_time = time.time()
        self._timer.start()

    def running(self):
        if self._timer:
            return True
        return False

