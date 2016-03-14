import unittest

from kyu_7.the_coins_of_ter import adjust


class AdjustTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(adjust(3, 0), 0)

    def test_equals_2(self):
        self.assertEqual(adjust(3, 1), 3)

    def test_equals_3(self):
        self.assertEqual(adjust(3, -2), 0)

    def test_equals_4(self):
        self.assertEqual(adjust(3, -4), -3)

    def test_equals_5(self):
        self.assertEqual(adjust(3, 3), 3)

    def test_equals_6(self):
        self.assertEqual(adjust(3, 6), 6)

    def test_equals_7(self):
        self.assertEqual(adjust(3, 7), 9)


if __name__ == '__main__':
    unittest.main()
