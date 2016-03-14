import unittest

from katas.kyu_7.genetic_algorithm_series_1_generate import generate


class GenerateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(len(generate(16)), 16)

    def test_equals_2(self):
        self.assertEqual(len(generate(32)), 32)

    def test_equals_3(self):
        self.assertEqual(len(generate(64)), 64)


if __name__ == '__main__':
    unittest.main()
