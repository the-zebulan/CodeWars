import unittest

from Kyu_8.find_the_slope import find_slope


class FindSlopeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_slope([19, 3, 20, 3]), '0')

    def test_equals_2(self):
        self.assertEqual(find_slope([-7, 2, -7, 4]), 'undefined')

    def test_equals_3(self):
        self.assertEqual(find_slope([10, 50, 30, 150]), '5')

    def test_equals_4(self):
        self.assertEqual(find_slope([10, 20, 20, 80]), '6')

    def test_equals_5(self):
        self.assertEqual(find_slope([-10, 6, -10, 3]), 'undefined')


if __name__ == '__main__':
    unittest.main()
