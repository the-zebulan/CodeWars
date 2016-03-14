import unittest

from Kyu_7.growth_of_a_population import nb_year


class GrowthOfAPopulationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(nb_year(1500, 5, 100, 5000), 15)

    def test_equals_2(self):
        self.assertEqual(nb_year(1500000, 2.5, 10000, 2000000), 10)

    def test_equals_3(self):
        self.assertEqual(nb_year(1500000, 0.25, 1000, 2000000), 94)


if __name__ == '__main__':
    unittest.main()
