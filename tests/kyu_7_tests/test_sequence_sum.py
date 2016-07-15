import unittest

from katas.kyu_7.sequence_sum import sum_of_n


class SequenceSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_of_n(3), [0, 1, 3, 6])

    def test_equals_2(self):
        self.assertEqual(sum_of_n(1), [0, 1])

    def test_equals_3(self):
        self.assertEqual(sum_of_n(0), [0])

    def test_equals_4(self):
        self.assertEqual(sum_of_n(-4), [0, -1, -3, -6, -10])
