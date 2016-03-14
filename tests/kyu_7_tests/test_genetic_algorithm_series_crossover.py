import unittest

from kyu_7.genetic_algorithm_series_crossover import crossover


class CrossoverTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(crossover('110', '001', 2), ['111', '000'])

    def test_equals_2(self):
        self.assertEqual(crossover('111000', '000110', 3),
                         ['111110', '000000'])


if __name__ == '__main__':
    unittest.main()
