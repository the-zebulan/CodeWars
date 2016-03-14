import unittest

from Kyu_5.two_joggers import nbr_of_laps


class NumberOfLapsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(nbr_of_laps(5, 3), [3, 5])

    def test_equals_2(self):
        self.assertEqual(nbr_of_laps(4, 6), [3, 2])

    def test_equals_3(self):
        self.assertEqual(nbr_of_laps(5, 5), [1, 1])


if __name__ == '__main__':
    unittest.main()
