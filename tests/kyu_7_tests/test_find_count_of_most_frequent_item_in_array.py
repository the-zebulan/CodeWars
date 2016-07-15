import unittest

from katas.kyu_7.find_count_of_most_frequent_item_in_array import \
    most_frequent_item_count


class MostFrequentItemCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(most_frequent_item_count([3, -1, -1]), 2)

    def test_equals_2(self):
        self.assertEqual(most_frequent_item_count(
            [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]), 5)

    def test_equals_3(self):
        self.assertEqual(most_frequent_item_count([]), 0)

    def test_equals_4(self):
        self.assertEqual(most_frequent_item_count([9]), 1)
