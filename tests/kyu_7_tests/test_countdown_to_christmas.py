import unittest
from datetime import date

from katas.kyu_7.countdown_to_christmas import days_until_christmas


class DaysUntilChristmasTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(days_until_christmas(date(2016, 12, 9)), 16)

    def test_equals_2(self):
        self.assertEqual(days_until_christmas(date(2016, 12, 8)), 17)

    def test_equals_3(self):
        self.assertEqual(days_until_christmas(date(1996, 12, 7)), 18)

    def test_equals_4(self):
        self.assertEqual(days_until_christmas(date(2015, 2, 23)), 305)

    def test_equals_5(self):
        self.assertEqual(days_until_christmas(date(2001, 7, 11)), 167)

    def test_equals_6(self):
        self.assertEqual(days_until_christmas(date(2000, 12, 9)), 16)

    def test_equals_7(self):
        self.assertEqual(days_until_christmas(date(1978, 3, 18)), 282)

    def test_equals_8(self):
        self.assertEqual(days_until_christmas(date(2016, 12, 25)), 0)

    def test_equals_9(self):
        self.assertEqual(days_until_christmas(date(2016, 12, 26)), 364)

    def test_equals_10(self):
        self.assertEqual(days_until_christmas(date(2015, 12, 26)), 365)


if __name__ == '__main__':
    unittest.main()
