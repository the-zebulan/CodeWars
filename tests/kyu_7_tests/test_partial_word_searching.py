import unittest

from katas.kyu_7.partial_word_searching import word_search


class WordSearchTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(word_search(
            'ab', ['za', 'ab', 'abc', 'zab', 'zbc']
        ), ['ab', 'abc', 'zab'])

    def test_equals_2(self):
        self.assertEqual(word_search(
            'aB', ['za', 'ab', 'abc', 'zab', 'zbc']
        ), ['ab', 'abc', 'zab'])

    def test_equals_3(self):
        self.assertEqual(word_search(
            'XX', ['za', 'ab', 'abc', 'zab', 'zbc']
        ), ['None'])


if __name__ == '__main__':
    unittest.main()
