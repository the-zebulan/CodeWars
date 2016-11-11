import unittest

from katas.kyu_7.more_than_zero import corrections


class CorrectionsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(corrections(8), '8 is more than zero.')

    def test_equal_2(self):
        self.assertEqual(corrections(1), '1 is more than zero.')

    def test_equal_3(self):
        self.assertEqual(corrections(-2), '-2 is equal to or less than zero.')

    def test_equal_4(self):
        self.assertEqual(corrections(-1), '-1 is equal to or less than zero.')

    def test_equal_5(self):
        self.assertEqual(corrections(0), '0 is equal to or less than zero.')
