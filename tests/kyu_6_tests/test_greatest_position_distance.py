import unittest

from kyu_6.greatest_position_distance import greatest_distance


class GreatestDistanceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(greatest_distance([0, 2, 1, 2, 4, 1]), 3)

    def test_equals_2(self):
        self.assertEqual(greatest_distance([9, 7, 1, 2, 3, 7, 0, -1, -2]), 4)

    def test_equals_3(self):
        self.assertEqual(greatest_distance([0, 7, 0, 2, 3, 7, 0, -1, -2]), 6)

    def test_equals_4(self):
        self.assertEqual(greatest_distance([1, 2, 3, 4]), 0)


if __name__ == '__main__':
    unittest.main()
