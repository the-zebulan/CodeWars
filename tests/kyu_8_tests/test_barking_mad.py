import unittest

from kyu_8.barking_mad import Dog


class DogTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(Dog("Beagle").bark(), 'Woof')

    def test_equals_2(self):
        self.assertEqual(Dog("Great Dane").bark(), 'Woof')

    def test_equals_3(self):
        self.assertEqual(Dog('Schnauzer').bark(), 'Woof')


if __name__ == '__main__':
    unittest.main()
