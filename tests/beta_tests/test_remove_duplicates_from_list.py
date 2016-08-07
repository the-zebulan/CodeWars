import unittest

from katas.beta.remove_duplicates_from_list import distinct


class DistinctTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(distinct([1]), [1])

    def test_equal_2(self):
        self.assertEqual(distinct([1, 2]), [1, 2])

    def test_equal_3(self):
        self.assertEqual(distinct([1, 1, 2]), [1, 2])

    def test_equal_4(self):
        self.assertEqual(distinct([1, 1, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_equal_5(self):
        self.assertEqual(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]),
                         [1, 2, 3, 4, 5, 6, 7])
