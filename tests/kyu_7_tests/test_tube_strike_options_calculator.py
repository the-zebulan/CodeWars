import unittest

from katas.kyu_7.tube_strike_options_calculator import calculator


class TubeStrikeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(calculator(5, 6, 1), 'Bus')

    def test_equals_2(self):
        self.assertEqual(calculator(4, 5, 1), 'Walk')

    def test_equals_3(self):
        self.assertEqual(calculator(5, 8, 0), 'Walk')

    def test_equals_4(self):
        self.assertEqual(calculator(5, 4, 3), 'Walk')

    def test_equals_5(self):
        self.assertEqual(calculator(11, 15, 2), 'Bus')

    def test_equals_6(self):
        self.assertEqual(calculator(0.6, 0.4, 0), 'Walk')


if __name__ == '__main__':
    unittest.main()
