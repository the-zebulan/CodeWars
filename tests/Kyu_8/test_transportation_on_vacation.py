import unittest

from Kyu_8.transportation_on_vacation import rental_car_cost


class RentalCarCostTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(rental_car_cost(1), 40)

    def test_equals_2(self):
        self.assertEqual(rental_car_cost(4), 140)

    def test_equals_3(self):
        self.assertEqual(rental_car_cost(7), 230)

    def test_equals_4(self):
        self.assertEqual(rental_car_cost(8), 270)


if __name__ == '__main__':
    unittest.main()
