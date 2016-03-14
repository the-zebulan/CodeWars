import unittest

from beta.permutation_average import permutation_average


class PermutationAverageTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(permutation_average(2), 2)

    def test_equals_2(self):
        self.assertEqual(permutation_average(25), 39)

    def test_equals_3(self):
        self.assertEqual(permutation_average(20), 11)

    def test_equals_4(self):
        self.assertEqual(permutation_average(737), 629)


if __name__ == '__main__':
    unittest.main()
