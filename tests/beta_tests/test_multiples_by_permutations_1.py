import unittest

from katas.beta.multiples_by_permutations_1 import search_permMult


class MultiplesByPermutationsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(search_permMult(10000, 7), 1)

    def test_equal_2(self):
        self.assertEqual(search_permMult(5000, 7), 0)

    def test_equal_3(self):
        self.assertEqual(search_permMult(10000, 4), 2)

    def test_equal_4(self):
        self.assertEqual(search_permMult(8000, 4), 1)

    def test_equal_5(self):
        self.assertEqual(search_permMult(5000, 3), 1)

    def test_equal_6(self):
        self.assertEqual(search_permMult(10000, 3), 2)


if __name__ == '__main__':
    unittest.main()
