import unittest

from katas.beta.most_frequent_weekdays import most_frequent_days


class MostFrequentWeekdaysTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(most_frequent_days(1084), ['Tuesday', 'Wednesday'])

    def test_equals_2(self):
        self.assertEqual(most_frequent_days(1167), ['Sunday'])

    def test_equals_3(self):
        self.assertEqual(most_frequent_days(1216), ['Friday', 'Saturday'])

    def test_equals_4(self):
        self.assertEqual(most_frequent_days(1492), ['Friday', 'Saturday'])

    def test_equals_5(self):
        self.assertEqual(most_frequent_days(1770), ['Monday'])

    def test_equals_6(self):
        self.assertEqual(most_frequent_days(1785), ['Saturday'])

    def test_equals_7(self):
        self.assertEqual(most_frequent_days(212), ['Wednesday', 'Thursday'])

    def test_equals_8(self):
        self.assertEqual(most_frequent_days(1), ['Monday'])

    def test_equals_9(self):
        self.assertEqual(most_frequent_days(2135), ['Saturday'])

    def test_equals_10(self):
        self.assertEqual(most_frequent_days(3043), ['Sunday'])

    def test_equals_11(self):
        self.assertEqual(most_frequent_days(2001), ['Monday'])

    def test_equals_12(self):
        self.assertEqual(most_frequent_days(3150), ['Sunday'])

    def test_equals_13(self):
        self.assertEqual(most_frequent_days(3230), ['Tuesday'])

    def test_equals_14(self):
        self.assertEqual(most_frequent_days(328), ['Monday', 'Sunday'])

    def test_equals_15(self):
        self.assertEqual(most_frequent_days(2016), ['Friday', 'Saturday'])

    def test_equals_16(self):
        self.assertEqual(most_frequent_days(334), ['Monday'])

    def test_equals_17(self):
        self.assertEqual(most_frequent_days(1986), ['Wednesday'])

    def test_equals_18(self):
        self.assertEqual(most_frequent_days(3361), ['Thursday'])

    def test_equals_19(self):
        self.assertEqual(most_frequent_days(5863), ['Thursday'])

    def test_equals_20(self):
        self.assertEqual(most_frequent_days(1910), ['Saturday'])

    def test_equals_21(self):
        self.assertEqual(most_frequent_days(1968), ['Monday', 'Tuesday'])

    def test_equals_22(self):
        self.assertEqual(most_frequent_days(7548), ['Thursday', 'Friday'])

    def test_equals_23(self):
        self.assertEqual(most_frequent_days(8116), ['Wednesday', 'Thursday'])

    def test_equals_24(self):
        self.assertEqual(most_frequent_days(9137), ['Friday'])

    def test_equals_25(self):
        self.assertEqual(most_frequent_days(1794), ['Wednesday'])


if __name__ == '__main__':
    unittest.main()
