import unittest

from katas.kyu_8.classy_extensions import Animal, Cat


class CatTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(Cat('Mr Whiskers').speak(), 'Mr Whiskers meows.')

    def test_equal_2(self):
        self.assertEqual(Cat('Lamp').speak(), 'Lamp meows.')

    def test_equal_3(self):
        self.assertEqual(Cat('$$Money Bags$$').speak(),
                         '$$Money Bags$$ meows.')

    def test_equal_4(self):
        self.assertEqual(Animal('Rover').speak(), 'Some other message?!?!')
