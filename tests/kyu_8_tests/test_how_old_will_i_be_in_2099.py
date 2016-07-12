import unittest

from katas.kyu_8.how_old_will_i_be_in_2099 import calculate_age


class CalculateAgeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(calculate_age(2012, 2016), 'You are 4 years old.')

    def test_equal_2(self):
        self.assertEqual(calculate_age(1989, 2016), 'You are 27 years old.')

    def test_equal_3(self):
        self.assertEqual(calculate_age(2000, 2090), 'You are 90 years old.')

    def test_equal_4(self):
        self.assertEqual(calculate_age(2000, 1990),
                         'You will be born in 10 years.')

    def test_equal_5(self):
        self.assertEqual(calculate_age(2000, 2000),
                         'You were born this very year!')

    def test_equal_6(self):
        self.assertEqual(calculate_age(900, 2900), 'You are 2000 years old.')

    def test_equal_7(self):
        self.assertEqual(calculate_age(2010, 1990),
                         'You will be born in 20 years.')

    def test_equal_8(self):
        self.assertEqual(calculate_age(2010, 1500),
                         'You will be born in 510 years.')

    def test_equal_9(self):
        self.assertEqual(calculate_age(2011, 2012), 'You are 1 year old.')

    def test_equal_10(self):
        self.assertEqual(calculate_age(2000, 1999),
                         'You will be born in 1 year.')


if __name__ == '__main__':
    unittest.main()
