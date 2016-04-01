import unittest

from katas.beta.unlucky_days import unlucky_days


class UnluckyDaysTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(unlucky_days(1634), 2)

    def test_equals_2(self):
        self.assertEqual(unlucky_days(2873), 2)

    def test_equals_3(self):
        self.assertEqual(unlucky_days(1586), 1)

    def test_equals_4(self):
        self.assertEqual(unlucky_days(2689), 2)

    def test_equals_5(self):
        self.assertEqual(unlucky_days(2819), 2)

    def test_equals_6(self):
        self.assertEqual(unlucky_days(2792), 2)

    def test_equals_7(self):
        self.assertEqual(unlucky_days(2723), 2)

    def test_equals_8(self):
        self.assertEqual(unlucky_days(1909), 1)

    def test_equals_9(self):
        self.assertEqual(unlucky_days(1812), 2)

    def test_equals_10(self):
        self.assertEqual(unlucky_days(1618), 2)

    def test_equals_11(self):
        self.assertEqual(unlucky_days(2132), 1)

    def test_equals_12(self):
        self.assertEqual(unlucky_days(2065), 3)

    def test_equals_13(self):
        self.assertEqual(unlucky_days(1594), 1)

    def test_equals_14(self):
        self.assertEqual(unlucky_days(2473), 2)

    def test_equals_15(self):
        self.assertEqual(unlucky_days(1797), 2)


if __name__ == '__main__':
    unittest.main()
