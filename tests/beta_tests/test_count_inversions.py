import unittest

from katas.beta.count_inversions import count_inversion


class CountInversionsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(count_inversion((1, 2, 5, 3, 4, 7, 6)), 3)

    def test_equal_2(self):
        self.assertEqual(count_inversion((0, 1, 2, 3)), 0)

    def test_equal_3(self):
        self.assertEqual(count_inversion((1, 2, 3)), 0)

    def test_equal_4(self):
        self.assertEqual(count_inversion((1, 3, 2)), 1)

    def test_equal_5(self):
        self.assertEqual(count_inversion((3, 6, 2, 7, 3)), 4)

    def test_equal_6(self):
        self.assertEqual(count_inversion(()), 0)

    def test_equal_7(self):
        self.assertEqual(count_inversion((3, 3, 3)), 0)


if __name__ == '__main__':
    unittest.main()
