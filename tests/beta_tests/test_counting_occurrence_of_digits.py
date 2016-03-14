import unittest

from beta.counting_occurrence_of_digits import List


class ListTestCase(unittest.TestCase):
    def setUp(self):
        self.lst = List()

    def test_equals(self):
        self.assertEqual(self.lst.count_spec_digits(
            [1, 1, 2, 3, 1, 2, 3, 4], [1, 3]), [(1, 3), (3, 2)])

    def test_equals_2(self):
        self.assertEqual(self.lst.count_spec_digits(
            [-18, -31, 81, -19, 111, -888], [1, 8, 4]),
            [(1, 7), (8, 5), (4, 0)])

    def test_equals_3(self):
        self.assertEqual(self.lst.count_spec_digits(
            [-77, -65, 56, -79, 6666, 222], [1, 8, 4]),
            [(1, 0), (8, 0), (4, 0)])

    def test_equals_4(self):
        self.assertEqual(self.lst.count_spec_digits(
            [], [1, 8, 4]), [(1, 0), (8, 0), (4, 0)])


if __name__ == '__main__':
    unittest.main()
