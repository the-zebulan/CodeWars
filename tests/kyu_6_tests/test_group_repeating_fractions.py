import unittest

from kyu_6.group_repeating_fractions import repeating_fractions


class RepeatingFractionsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(repeating_fractions(1, 1), '1.0')

    def test_equals_2(self):
        self.assertEqual(repeating_fractions(1, 2), '0.5')

    def test_equals_3(self):
        self.assertEqual(repeating_fractions(1, 3), '0.(3)')

    def test_equals_4(self):
        self.assertEqual(repeating_fractions(2, 888), '0.(0)(2)5(2)5(2)5(2)5')

    def test_equals_5(self):
        self.assertEqual(repeating_fractions(1554, 70), '22.2')

    def test_equals_6(self):
        self.assertEqual(repeating_fractions(11, 7), '1.57142857143')

    def test_equals_7(self):
        self.assertEqual(repeating_fractions(15, 7), '2.14285714286')

    def test_equals_8(self):
        self.assertEqual(repeating_fractions(32, 11), '2.90909090909')


if __name__ == '__main__':
    unittest.main()
