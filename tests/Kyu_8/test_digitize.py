import unittest

from Kyu_8.digitize import digitize


class DigitizeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(digitize(35231), [1, 3, 2, 5, 3])

    def test_equals_2(self):
        self.assertEqual(digitize(12345), [5, 4, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
