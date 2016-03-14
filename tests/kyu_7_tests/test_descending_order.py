import unittest

from katas.kyu_7.descending_order import Descending_Order


class DescendingOrderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Descending_Order(0), 0)

    def test_equals_2(self):
        self.assertEqual(Descending_Order(15), 51)

    def test_equals_3(self):
        self.assertEqual(Descending_Order(123456789), 987654321)


if __name__ == '__main__':
    unittest.main()
