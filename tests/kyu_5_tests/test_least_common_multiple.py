import unittest

from Kyu_5.least_common_multiple import lcm


class LeastCommonMultipleTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(lcm(2, 5), 10)

    def test_equals_2(self):
        self.assertEqual(lcm(2, 3, 4), 12)

    def test_equals_3(self):
        self.assertEqual(lcm(9), 9)

    def test_equals_4(self):
        self.assertEqual(lcm(0), 0)

    def test_equals_5(self):
        self.assertEqual(lcm(0, 1), 0)


if __name__ == '__main__':
    unittest.main()
