import unittest

from katas.kyu_8.powers_of_2 import powers_of_two


class PowersOfTwoTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(powers_of_two(0), [1])

    def test_equal_2(self):
        self.assertEqual(powers_of_two(1), [1, 2])

    def test_equal_3(self):
        self.assertEqual(powers_of_two(4), [1, 2, 4, 8, 16])
