import unittest

from beta.variance_in_array_of_words import variance


class VarianceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(variance(['Hello', 'World']), 0)

    def test_equals_2(self):
        self.assertEqual(variance(['Hi', 'World']), 2.25)


if __name__ == '__main__':
    unittest.main()
