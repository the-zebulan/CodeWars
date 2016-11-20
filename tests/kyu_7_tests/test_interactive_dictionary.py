import unittest

from katas.kyu_7.interactive_dictionary import Dictionary


class DictionaryTestCase(unittest.TestCase):
    def setUp(self):
        self.d = Dictionary()

    def test_equal_1(self):
        key = 'Apple'
        value = 'A Fruit that grows on trees'
        self.d.newentry(key, value)
        self.assertEqual(self.d.look(key), value)

    def test_equal_2(self):
        self.assertEqual(self.d.look('Banana'), "Can't find entry for Banana")


if __name__ == '__main__':
    unittest.main()
