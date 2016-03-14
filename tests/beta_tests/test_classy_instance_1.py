import unittest

from beta.classy_instance_1 import show_me


class ClassyTestCase(unittest.TestCase):
    def test_equals(self):
        porsche = Vehicle(2, 4, 'Gas')
        self.assertEqual(show_me(porsche), 'Hi, I\'m one of those Vehicles! '
                                           'Have a look at my engine, seats '
                                           'and wheels.')

    def test_equals_2(self):
        earth = Planet('moon')
        self.assertEqual(show_me(earth), 'Hi, I\'m one of those Planets! Have'
                                         ' a look at my moon.')


class Vehicle:
    def __init__(self, seats, wheels, engine):
        self.seats = seats
        self.wheels = wheels
        self.engine = engine


class Planet:
    def __init__(self, moon):
        self.moon = moon


if __name__ == '__main__':
    unittest.main()
