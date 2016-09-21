import unittest

from katas.beta.how_much_coffee_do_you_need import how_much_coffee


class HowMuchCoffeeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(how_much_coffee([]), 0)

    def test_equal_2(self):
        self.assertEqual(how_much_coffee(['cw']), 1)

    def test_equal_3(self):
        self.assertEqual(how_much_coffee(['CW']), 2)

    def test_equal_4(self):
        self.assertEqual(how_much_coffee(['cw', 'CAT']), 3)

    def test_equal_5(self):
        self.assertEqual(how_much_coffee(['cw', 'CAT', 'DOG']),
                         'You need extra sleep')

    def test_equal_6(self):
        self.assertEqual(how_much_coffee(['cw', 'CAT', 'cw=others']), 3)
