import unittest

from beta.no_duplicates_here import list_de_dup


class ListDeDuplicateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(list_de_dup(['g', 3, 'a', 'a']), [3, 'a', 'g'])

    def test_equals_2(self):
        self.assertEqual(list_de_dup([1, 2, 3, 4, 1, 2, 3, 4]), [1, 2, 3, 4])

    def test_equals_3(self):
        self.assertEqual(list_de_dup([
            'code', 'wars', 'ain\'t', None, None, 'code', 'wars', 'ain\'t',
            'the', 'same', 'as', 'the', 'rest']),
            ['ain\'t', 'as', 'code', 'rest', 'same', 'the', 'wars'])


if __name__ == '__main__':
    unittest.main()
