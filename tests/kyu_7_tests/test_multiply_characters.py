import unittest

from kyu_7.multiply_characters import spam


class SpamTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(spam(1), 'hue')

    def test_equals_2(self):
        self.assertEqual(spam(6), 'huehuehuehuehuehue')

    def test_equals_3(self):
        self.assertEqual(spam(14),
                         'huehuehuehuehuehuehuehuehuehuehuehuehuehue')


if __name__ == '__main__':
    unittest.main()
