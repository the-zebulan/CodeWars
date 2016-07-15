import unittest

from katas.beta.nothing_special import nothing_special


class NothingSpecialTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(nothing_special('Hello World!'), 'Hello World')

    def test_equals_2(self):
        self.assertEqual(nothing_special('%^Take le$ft ##quad%r&a&nt'),
                         'Take left quadrant')

    def test_equals_3(self):
        self.assertEqual(nothing_special('M$$$$$$$y ally!!!!!'), 'My ally')

    def test_equals_4(self):
        self.assertEqual(nothing_special(25), 'Not a string!')
