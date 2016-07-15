import unittest

from katas.kyu_8.grasshopper_summation import summation


class SummationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(summation(1), 1)

    def test_equals_2(self):
        self.assertEqual(summation(8), 36)
