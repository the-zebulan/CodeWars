import unittest

from katas.kyu_6.find_the_parity_outlier import find_outlier


class FindOutlierTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)

    def test_equals_2(self):
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)

    def test_equals_3(self):
        self.assertEqual(find_outlier([2, 6, 8, 10, 3]), 3)


if __name__ == '__main__':
    unittest.main()
