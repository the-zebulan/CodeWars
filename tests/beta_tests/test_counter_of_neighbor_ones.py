import unittest

from katas.beta.counter_of_neighbor_ones import ones_counter


class OnesCounterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(ones_counter([0]), [])

    def test_equals_2(self):
        self.assertEqual(ones_counter([1, 0, 1, 1]), [1, 2])

    def test_equals_3(self):
        self.assertEqual(ones_counter([0, 0, 0, 0, 0, 0, 0, 0]), [])

    def test_equals_4(self):
        self.assertEqual(ones_counter([1, 1, 1, 1, 1]), [5])

    def test_equals_5(self):
        self.assertEqual(
            ones_counter([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]), [3, 1, 2]
        )

    def test_equals_6(self):
        self.assertEqual(ones_counter([0, 0, 0, 1, 0, 0, 1, 1]), [1, 2])

    def test_equals_7(self):
        self.assertEqual(
            ones_counter([1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1]),
            [1, 2, 4, 1]
        )
