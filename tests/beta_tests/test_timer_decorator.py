import unittest
from time import sleep

from katas.beta.timer_decorator import timer


class TimerDecoratorTestCase(unittest.TestCase):
    def test_true_1(self):
        @timer(1)
        def foo():
            sleep(0.1)
        self.assertTrue(foo())

    def test_false_1(self):
        @timer(1)
        def bar():
            sleep(1.1)
        self.assertFalse(bar())
