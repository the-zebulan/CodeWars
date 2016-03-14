import unittest

from Kyu_6.urban_dictionary import WordDictionary


class WordDictionaryTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = WordDictionary()
        self.wd.add_word('a')
        self.wd.add_word('at')
        self.wd.add_word('ate')
        self.wd.add_word('ear')

        self.wd2 = WordDictionary()
        self.wd2.add_word('co')
        self.wd2.add_word('cod')
        self.wd2.add_word('code')
        self.wd2.add_word('codewars')

    def test_true(self):
        self.assertTrue(self.wd.search('a'))

    def test_true_2(self):
        self.assertTrue(self.wd.search('a.'))

    def test_true_3(self):
        self.assertTrue(self.wd.search('a.e'))

    def test_true_4(self):
        self.assertTrue(self.wd.search('ea.'))

    def test_true_5(self):
        self.assertTrue(self.wd2.search('........'))

    def test_true_6(self):
        self.assertTrue(self.wd2.search('cod.'))

    def test_true_7(self):
        self.assertTrue(self.wd2.search('co..w..s'))

    def test_false(self):
        self.assertFalse(self.wd.search('b'))

    def test_false_2(self):
        self.assertFalse(self.wd.search('e.'))

    def test_false_3(self):
        self.assertFalse(self.wd.search('ea..'))

    def test_false_4(self):
        self.assertFalse(self.wd2.search('c.o'))

    def test_false_5(self):
        self.assertFalse(self.wd2.search('c.o'))

    def test_false_6(self):
        self.assertFalse(self.wd2.search('co..w..'))


if __name__ == '__main__':
    unittest.main()
