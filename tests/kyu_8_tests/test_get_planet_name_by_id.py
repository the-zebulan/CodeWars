import unittest

from katas.kyu_8.get_planet_name_by_id import get_planet_name


class GetPlanetNameTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_planet_name(2), 'Venus')

    def test_equals_2(self):
        self.assertEqual(get_planet_name(5), 'Jupiter')

    def test_equals_3(self):
        self.assertEqual(get_planet_name(3), 'Earth')

    def test_equals_4(self):
        self.assertEqual(get_planet_name(4), 'Mars')

    def test_equals_5(self):
        self.assertEqual(get_planet_name(8), 'Neptune')

    def test_equals_6(self):
        self.assertEqual(get_planet_name(1), 'Mercury')
