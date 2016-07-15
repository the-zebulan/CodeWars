import unittest

from katas.kyu_7.looking_for_a_benefactor import new_avg


class NewAverageTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(new_avg([
            129306, 37783, 169930, 177970, 66848, 68272, 120258, 10307,
            162807, 54503, 66465, 177701, 144296, 171044, 126332, 144744,
            177657, 61511, 128350, 52167, 103604, 110178, 115495, 97452,
            127971, 36683, 190742, 10960, 183186
        ], 120389.413793), 387161)

    def test_equals_2(self):
        self.assertEqual(new_avg([14, 30, 5, 7, 9, 11, 16], 90), 628)

    def test_equals_3(self):
        self.assertEqual(new_avg([14, 30, 5, 7, 9, 11, 15], 92), 645)

    def test_exception(self):
        self.assertRaises(ValueError, new_avg, [0, 0], 0)
