import unittest

from kyu_7.genetic_algorithm_series_2_mutation import mutate


class MutateTestCase(unittest.TestCase):
    def setUp(self):
        self.zero = '0' * 100
        self.one = '1' * 100

    def test_equals(self):
        self.assertEqual(mutate(self.zero, 1), self.one)

    def test_equals_2(self):
        self.assertEqual(mutate(self.one, 1), self.zero)

    def test_equals_3(self):
        self.assertEqual(mutate(self.zero, 0), self.zero)

    def test_equals_4(self):
        self.assertEqual(mutate(self.one, 0), self.one)


if __name__ == '__main__':
    unittest.main()
