import unittest

from kyu_6.grouped_by_commas import group_by_commas


class GroupByCommasTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(group_by_commas(1), '1')

    def test_equals_2(self):
        self.assertEqual(group_by_commas(10), '10')

    def test_equals_3(self):
        self.assertEqual(group_by_commas(100), '100')

    def test_equals_4(self):
        self.assertEqual(group_by_commas(1000), '1,000')

    def test_equals_5(self):
        self.assertEqual(group_by_commas(10000), '10,000')

    def test_equals_6(self):
        self.assertEqual(group_by_commas(100000), '100,000')

    def test_equals_7(self):
        self.assertEqual(group_by_commas(1000000), '1,000,000')

    def test_equals_8(self):
        self.assertEqual(group_by_commas(35235235), '35,235,235')


if __name__ == '__main__':
    unittest.main()
