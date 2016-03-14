import unittest

from katas.kyu_6.single_word_pig_latin import pig_latin


class PigLatinTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pig_latin('map'), 'apmay')

    def test_equals_2(self):
        self.assertEqual(pig_latin('egg'), 'eggway')

    def test_equals_3(self):
        self.assertEqual(pig_latin('spaghetti'), 'aghettispay')


if __name__ == '__main__':
    unittest.main()
