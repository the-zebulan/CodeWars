import unittest

from beta.sum_of_all_arguments import sum_all


class SumAllTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sum_all(6, 2, 3), 11)

    def test_equals_2(self):
        self.assertEqual(sum_all(756, 2, 1, 10), 769)

    def test_equals_3(self):
        self.assertEqual(sum_all(76856, -32, 1981, 1076), 79881)

    def test_equals_4(self):
        self.assertEqual(sum_all(7, -3452, 1981, 1076), -388)

    def test_false(self):
        self.assertFalse(sum_all(1, -32, "codewars", 1076))


if __name__ == '__main__':
    unittest.main()
