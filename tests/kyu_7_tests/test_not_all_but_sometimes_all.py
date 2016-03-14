import unittest

from katas.kyu_7.not_all_but_sometimes_all import remove


class RemoveTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(remove('this is a string', {'t': 1, 'i': 2}),
                         'hs s a string')

    def test_equals_2(self):
        self.assertEqual(remove('hello world', {'x': 5, 'i': 2}),
                         'hello world')

    def test_equals_3(self):
        self.assertEqual(remove('apples and bananas', {'a': 50, 'n': 1}),
                         'pples d bnns')

    def test_equals_4(self):
        self.assertEqual(remove('a', {'a': 1, 'n': 1}), '')

    def test_equals_5(self):
        self.assertEqual(remove(
            'codewars', {'c': 5, 'o': 1, 'd': 1, 'e': 1, 'w': 1, 'z': 1,
                         'a': 1, 'r': 1, 's': 1}
        ), '')


if __name__ == '__main__':
    unittest.main()
