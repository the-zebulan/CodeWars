import unittest

from katas.kyu_7.most_frequent_elements import find_most_frequent


class FindMostFrequentTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_most_frequent([1, 1, 2, 3]), {1})

    def test_equals_2(self):
        self.assertEqual(find_most_frequent([1, 1, 2, 2, 3]), {1, 2})

    def test_equals_3(self):
        self.assertEqual(find_most_frequent([1, 1, '2', '2', 3]), {1, '2'})


if __name__ == '__main__':
    unittest.main()
