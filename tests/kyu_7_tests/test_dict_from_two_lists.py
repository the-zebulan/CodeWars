import unittest

from katas.kyu_7.dict_from_two_lists import createDict


class CreateDictTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]),
                         {'a': 1, 'b': 2, 'c': 3, 'd': None})

    def test_equals_2(self):
        self.assertEqual(createDict(['a', 'b', 'c'], [1, 2, 3, 4]),
                         {'a': 1, 'b': 2, 'c': 3})


if __name__ == '__main__':
    unittest.main()
