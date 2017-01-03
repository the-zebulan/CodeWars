import unittest

from katas.kyu_5.airport_arrivals_departures_1 import flap_display


class FlapDisplayTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(flap_display(['CAT'], [[1, 13, 27]]), ['DOG'])

    def test_equal_2(self):
        self.assertEqual(
            flap_display(['HELLO '], [[15, 49, 50, 48, 43, 13]]), ['WORLD!'])

    def test_equal_3(self):
        self.assertEqual(flap_display(['CODE'], [[20, 20, 28, 0]]), ['WARS'])
