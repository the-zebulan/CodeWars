import unittest

from Kyu_7.greatest_common_divisor import mygcd


class MyGCDTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(mygcd(30, 12), 6)

    def test_equals_2(self):
        self.assertEqual(mygcd(8, 9), 1)

    def test_equals_3(self):
        self.assertEqual(mygcd(1, 1), 1)

    def test_equals_4(self):
        self.assertEqual(mygcd(74634, 73865), 1)

    def test_equals_5(self):
        self.assertEqual(mygcd(10927782, 6902514), 846)

    def test_equals_6(self):
        self.assertEqual(mygcd(1590771464, 1590771620), 4)


if __name__ == '__main__':
    unittest.main()
