import unittest

from katas.kyu_6.wordify import wordify


class WordifyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(wordify(1), 'one')

    def test_equals_2(self):
        self.assertEqual(wordify(10), 'ten')

    def test_equals_3(self):
        self.assertEqual(wordify(12), 'twelve')

    def test_equals_4(self):
        self.assertEqual(wordify(17), 'seventeen')

    def test_equals_5(self):
        self.assertEqual(wordify(56), 'fifty six')

    def test_equals_6(self):
        self.assertEqual(wordify(90), 'ninety')

    def test_equals_7(self):
        self.assertEqual(wordify(100), 'one hundred')

    def test_equals_8(self):
        self.assertEqual(wordify(120), 'one hundred twenty')

    def test_equals_9(self):
        self.assertEqual(wordify(326), 'three hundred twenty six')


if __name__ == '__main__':
    unittest.main()
