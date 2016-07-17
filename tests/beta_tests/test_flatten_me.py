import unittest

from katas.beta.flatten_me import flatten_me


class FlattenMeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(flatten_me([1, [2, 3], 4]), [1, 2, 3, 4])

    def test_equal_2(self):
        self.assertEqual(flatten_me([[1, 2], [3, 4]]), [1, 2, 3, 4])

    def test_equal_3(self):
        self.assertEqual(flatten_me([1, [2], [3], [4]]), [1, 2, 3, 4])

    def test_equal_4(self):
        self.assertEqual(flatten_me(['a', ['b', 'd']]), ['a', 'b', 'd'])

    def test_equal_5(self):
        self.assertEqual(
            flatten_me(['c', ['b', 'a', 'x']]), ['c', 'b', 'a', 'x']
        )

    def test_equal_6(self):
        self.assertEqual(
            flatten_me([['a', 'b'], 'c', ['d']]), ['a', 'b', 'c', 'd']
        )

    def test_equal_7(self):
        self.assertEqual(flatten_me(
            [[True, False], '!', '?', 99, [71, '@', True]]
        ), [True, False, '!', '?', 99, 71, '@', True])
