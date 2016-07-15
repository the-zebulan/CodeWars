import unittest

from katas.beta.lowest_product_of_4_consecutive_nums import lowest_product


class LowestProductTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(lowest_product('123456789'), 24)

    def test_equals_2(self):
        self.assertEqual(lowest_product('2345611117899'), 1)

    def test_equals_3(self):
        self.assertEqual(lowest_product('2305611117899'), 0)

    def test_equals_4(self):
        self.assertEqual(lowest_product('333'), 'Number is too small')

    def test_equals_5(self):
        self.assertEqual(lowest_product('1234111'), 4)
