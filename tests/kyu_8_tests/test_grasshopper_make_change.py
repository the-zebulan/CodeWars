import unittest

from katas.kyu_8.grasshopper_make_change import (
    candy, change, chips, money, soda
)


class MakeChangeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(candy, 1.42)

    def test_equals_2(self):
        self.assertEqual(change, 5.18)

    def test_equals_3(self):
        self.assertEqual(chips, 2.4)

    def test_equals_4(self):
        self.assertEqual(money, 10)

    def test_equals_5(self):
        self.assertEqual(soda, 1)


if __name__ == '__main__':
    unittest.main()
