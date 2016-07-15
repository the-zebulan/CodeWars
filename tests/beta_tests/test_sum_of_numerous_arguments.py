import unittest

from katas.beta.sum_of_numerous_arguments import find_sum


class FindSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_sum(1, 3, 5), 9)

    def test_equals_2(self):
        self.assertEqual(find_sum(), 0)

    def test_equals_3(self):
        self.assertEqual(find_sum(1, -2, 4), -1)

    def test_equals_4(self):
        self.assertEqual(find_sum(0), 0)

    def test_equals_5(self):
        self.assertEqual(find_sum(1, 1, 5), 7)

    def test_equals_6(self):
        self.assertEqual(find_sum(1, 1, 1, 1, 1, 1, 1, 1, 0), 8)

    def test_equals_7(self):
        self.assertEqual(find_sum(-1, -1, 5), -1)

    def test_equals_8(self):
        self.assertEqual(find_sum(-1, -1, -5), -1)

    def test_equals_9(self):
        self.assertEqual(find_sum(0, -1, 5), -1)

    def test_equals_10(self):
        self.assertEqual(find_sum(0, 0, 0), 0)
