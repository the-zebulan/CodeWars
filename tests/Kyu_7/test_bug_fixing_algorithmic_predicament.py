import unittest

from Kyu_7.bug_fixing_algorithmic_predicament import highest_age


class HighestAgeTestCase(unittest.TestCase):
    def setUp(self):
        self.g1 = [{'name': 'kay', 'age': 1}, {'name': 'john', 'age': 13},
                   {'name': 'kay', 'age': 76}]
        self.g2 = [{'name': 'john', 'age': 1}, {'name': 'alice', 'age': 76}]

    def test_equals(self):
        self.assertEqual(highest_age(self.g1, [
            {'name': 'john', 'age': 1}, {'name': 'alice', 'age': 77}
        ]), 'alice')

    def test_equals_2(self):
        self.assertEqual(highest_age(self.g1, self.g2), 'kay')

    def test_equals_3(self):
        self.assertEqual(highest_age([
            {'name': 'kay', 'age': 1}, {'name': 'john', 'age': 130},
            {'name': 'kay', 'age': 76}
        ], self.g2), 'john')

    def test_equals_4(self):
        self.assertEqual(highest_age([
            {'name': 'kay', 'age': 1}, {'name': 'john', 'age': 130},
            {'name': 'kay', 'age': 130}
        ], self.g2), 'john')

    def test_equals_5(self):
        self.assertEqual(highest_age([
            {'name': 'kay', 'age': 2}, {'name': 'john', 'age': 130},
            {'name': 'kay', 'age': 130}
        ], self.g2), 'kay')


if __name__ == '__main__':
    unittest.main()
