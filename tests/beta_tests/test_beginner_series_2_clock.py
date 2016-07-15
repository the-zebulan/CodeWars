import unittest

from katas.beta.beginner_series_2_clock import past


class PastTestCase(unittest.TestCase):
    def test_equals_(self):
        self.assertEqual(past(0, 1, 1), 61000)

    def test_equals_2(self):
        self.assertEqual(past(1, 1, 1), 3661000)

    def test_equals_3(self):
        self.assertEqual(past(0, 0, 0), 0)

    def test_equals_4(self):
        self.assertEqual(past(1, 0, 1), 3601000)

    def test_equals_5(self):
        self.assertEqual(past(1, 0, 0), 3600000)
