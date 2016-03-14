import unittest

from kyu_8.days_in_the_year import year_days


class YearDaysTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(year_days(0), '0 has 366 days')

    def test_equals_2(self):
        self.assertEqual(year_days(-64), '-64 has 366 days')

    def test_equals_3(self):
        self.assertEqual(year_days(2016), '2016 has 366 days')

    def test_equals_4(self):
        self.assertEqual(year_days(1974), '1974 has 365 days')

    def test_equals_5(self):
        self.assertEqual(year_days(-10), '-10 has 365 days')

    def test_equals_6(self):
        self.assertEqual(year_days(666), '666 has 365 days')

    def test_equals_7(self):
        self.assertEqual(year_days(1857), '1857 has 365 days')

    def test_equals_8(self):
        self.assertEqual(year_days(2000), '2000 has 366 days')

    def test_equals_9(self):
        self.assertEqual(year_days(-300), '-300 has 365 days')

    def test_equals_10(self):
        self.assertEqual(year_days(-1), '-1 has 365 days')


if __name__ == '__main__':
    unittest.main()
