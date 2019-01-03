
class Lowpass(object):
    def __init__(self, tau, ts):
        self._a = 1. / (tau / ts + 1.)
        self._b = tau / ts / (tau / ts + 1.)
        self._last_value = 0.
        self._ready = False

    def filter(self, val):
        if self._ready:
            val = self._a * val + self._b * self._last_value
        else:
            self._ready = True
        self._last_value = val
        return val

    @property
    def last_value(self):
        return self._last_value
