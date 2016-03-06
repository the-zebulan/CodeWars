import unittest

from Kyu_7.some_circles import sum_circles


class SumCirclesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_circles(2), 'We have this much circle: 3')

    def test_equals_2(self):
        self.assertEqual(sum_circles(2, 3, 4), 'We have this much circle: 23')

    def test_equals_3(self):
        self.assertEqual(sum_circles(48, 7, 8, 9, 10),
                         'We have this much circle: 2040')

    def test_equals_4(self):
        self.assertEqual(sum_circles(1), 'We have this much circle: 1')

    def test_equals_5(self):
        self.assertEqual(sum_circles(1, 1, 1, 2, 3, 4, 5),
                         'We have this much circle: 45')


if __name__ == '__main__':
    unittest.main()
