import unittest

from Kyu_8.classy_extensions import Cat


class CatTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Cat('Mr Whiskers').speak(), 'Mr Whiskers meows.')

    def test_equals_2(self):
        self.assertEqual(Cat('Lamp').speak(), 'Lamp meows.')

    def test_equals_3(self):
        self.assertEqual(Cat('$$Money Bags$$').speak(),
                         '$$Money Bags$$ meows.')


if __name__ == '__main__':
    unittest.main()
