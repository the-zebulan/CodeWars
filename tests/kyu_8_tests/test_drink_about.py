import unittest

from kyu_8.drink_about import people_with_age_drink


class DrinkTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(people_with_age_drink(13), 'drink toddy')

    def test_equals_2(self):
        self.assertEqual(people_with_age_drink(17), 'drink coke')

    def test_equals_3(self):
        self.assertEqual(people_with_age_drink(18), 'drink beer')

    def test_equals_4(self):
        self.assertEqual(people_with_age_drink(20), 'drink beer')

    def test_equals_5(self):
        self.assertEqual(people_with_age_drink(30), 'drink whisky')


if __name__ == '__main__':
    unittest.main()
