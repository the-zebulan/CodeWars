import unittest

from katas.kyu_5.weight_for_weight import order_weight


class OrderWeightTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(order_weight('56 65 74 100 99 68 86 180 90'),
                         '100 180 90 56 65 74 68 86 99')

    def test_equals_2(self):
        self.assertEqual(order_weight('103 123 4444 99 2000'),
                         '2000 103 123 4444 99')

    def test_equals_3(self):
        self.assertEqual(order_weight(
            '2000 10003 1234000 44444444 9999 11 11 22 123'),
            '11 11 2000 10003 22 123 1234000 44444444 9999')
