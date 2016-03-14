import unittest

from kyu_5.simple_pig_latin import pig_it


class PigLatinTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pig_it('Pig latin is cool'),
                         'igPay atinlay siay oolcay')

    def test_equals_2(self):
        self.assertEqual(pig_it('This is my string'),
                         'hisTay siay ymay tringsay')


if __name__ == '__main__':
    unittest.main()
