import unittest

from beta.how_many_numbers import sel_number


class HowManyNumbersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sel_number(0, 1), 0)

    def test_equals_2(self):
        self.assertEqual(sel_number(3, 1), 0)

    def test_equals_3(self):
        self.assertEqual(sel_number(13, 1), 1)

    def test_equals_4(self):
        self.assertEqual(sel_number(20, 2), 2)

    def test_equals_5(self):
        self.assertEqual(sel_number(30, 2), 4)

    def test_equals_6(self):
        self.assertEqual(sel_number(44, 2), 6)

    def test_equals_7(self):
        self.assertEqual(sel_number(50, 3), 12)


if __name__ == '__main__':
    unittest.main()
