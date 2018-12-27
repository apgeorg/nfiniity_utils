import unittest
from nfiniity_utils.nfiniity_utils.timer import Timer

class TestTimer(unittest.TestCase):

    def timeout(self, name):
        print("Timeout: " + name)

    def test_init(self):
        t = Timer(1, self.timeout, oneshot=True, args=["test_init"])
        self.assertIsNotNone(t)

    def test_start(self):
        t = Timer(1, self.timeout, oneshot=True, args=["test_start"])
        t.start()
        self.assertEqual(t.running, True)

    def test_stop(self):
        t = Timer(1, self.timeout, oneshot=True, args=["test_stop"])
        t.start()
        t.stop()
        self.assertEqual(t.running, False)

if __name__ == '__main__':
    unittest.main()