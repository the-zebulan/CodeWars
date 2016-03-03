import unittest

from Kyu_4.permutations import permutations


class PermutationsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sorted(permutations('a')), ['a'])

    def test_equals_2(self):
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])

    def test_equals_3(self):
        self.assertEqual(sorted(permutations('aabb')),
                         ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


if __name__ == '__main__':
    unittest.main()
