import unittest

from Kyu_8.count_by_x import count_by


class CountByXTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(count_by(1, 5), [1, 2, 3, 4, 5])

    def test_equals_2(self):
        self.assertEqual(count_by(2, 5), [2, 4, 6, 8, 10])

    def test_equals_3(self):
        self.assertEqual(count_by(3, 5), [3, 6, 9, 12, 15])

    def test_equals_4(self):
        self.assertEqual(count_by(50, 5), [50, 100, 150, 200, 250])

    def test_equals_5(self):
        self.assertEqual(count_by(100, 5), [100, 200, 300, 400, 500])


if __name__ == '__main__':
    unittest.main()
