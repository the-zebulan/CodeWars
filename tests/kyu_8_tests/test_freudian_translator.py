import unittest

from katas.kyu_8.freudian_translator import to_freud


class ToFreudTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(to_freud('test'), 'sex')

    def test_equal_2(self):
        self.assertEqual(to_freud('sexy sex'), 'sex sex')

    def test_equal_3(self):
        self.assertEqual(to_freud('This is a test'), 'sex sex sex sex')

    def test_equal_4(self):
        self.assertEqual(to_freud('This is a longer test'),
                         'sex sex sex sex sex')

    def test_equal_5(self):
        self.assertEqual(to_freud("You're becoming a true freudian expert"),
                         'sex sex sex sex sex sex')
