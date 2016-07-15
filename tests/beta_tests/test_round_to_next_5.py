import unittest

from katas.beta.round_to_next_5 import round_to_next5


class RoundToNextFiveTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(round_to_next5(0), 0)

    def test_equals_2(self):
        self.assertEqual(round_to_next5(1), 5)

    def test_equals_3(self):
        self.assertEqual(round_to_next5(5), 5)

    def test_equals_4(self):
        self.assertEqual(round_to_next5(7), 10)

    def test_equals_5(self):
        self.assertEqual(round_to_next5(20), 20)

    def test_equals_6(self):
        self.assertEqual(round_to_next5(39), 40)
