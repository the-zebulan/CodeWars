import unittest

from kyu_6.almost_even import splitInteger


class SplitIntegerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(splitInteger(20, 6), [3, 3, 3, 3, 4, 4])

    def test_equals_2(self):
        self.assertEqual(splitInteger(10, 1), [10])

    def test_equals_3(self):
        self.assertEqual(splitInteger(2, 2), [1, 1])

    def test_equals_4(self):
        self.assertEqual(splitInteger(20, 5), [4, 4, 4, 4, 4])


if __name__ == '__main__':
    unittest.main()
