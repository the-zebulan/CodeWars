import unittest

from Kyu_7.consecutive_numbers_needed import consecutive


class ConsecutiveTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(consecutive([4, 8, 6]), 2)

    def test_equals_2(self):
        self.assertEqual(consecutive([1, 2, 3, 4]), 0)

    def test_equals_3(self):
        self.assertEqual(consecutive([]), 0)

    def test_equals_4(self):
        self.assertEqual(consecutive([1]), 0)

    def test_equals_5(self):
        self.assertEqual(consecutive([-10]), 0)


if __name__ == '__main__':
    unittest.main()
