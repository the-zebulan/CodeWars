import unittest

from katas.kyu_6.single_word_pig_latin import pig_latin


class PigLatinTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(pig_latin('map'), 'apmay')

    def test_equal_2(self):
        self.assertEqual(pig_latin('egg'), 'eggway')

    def test_equal_3(self):
        self.assertEqual(pig_latin('spaghetti'), 'aghettispay')

    def test_equal_4(self):
        self.assertEqual(pig_latin('zqxy'), 'zqxyay')

    def test_is_none_1(self):
        self.assertIsNone(pig_latin(''))

    def test_is_none_2(self):
        self.assertIsNone(pig_latin('!@#$%'))
