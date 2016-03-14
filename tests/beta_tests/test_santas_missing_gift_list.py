import unittest

from katas.beta.santas_missing_gift_list import gifts


class GiftsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(gifts(1), ['Toy Soldier'])

    def test_equals_2(self):
        self.assertEqual(gifts(2), ['Wooden Train'])

    def test_equals_3(self):
        self.assertEqual(gifts(3), ['Toy Soldier', 'Wooden Train'])

    def test_equals_4(self):
        self.assertEqual(gifts(22), ['Hoop', 'Horse', 'Wooden Train'])

    def test_equals_5(self):
        self.assertEqual(gifts(160), ['Football', 'Teddy'])


if __name__ == '__main__':
    unittest.main()
