import unittest

from kyu_4.next_bigger_number_with_same_digits import next_bigger


class NextBiggerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(next_bigger(12), 21)

    def test_equals_2(self):
        self.assertEqual(next_bigger(513), 531)

    def test_equals_3(self):
        self.assertEqual(next_bigger(2017), 2071)

    def test_equals_4(self):
        self.assertEqual(next_bigger(9), -1)

    def test_equals_5(self):
        self.assertEqual(next_bigger(111), -1)

    def test_equals_6(self):
        self.assertEqual(next_bigger(531), -1)


if __name__ == '__main__':
    unittest.main()
