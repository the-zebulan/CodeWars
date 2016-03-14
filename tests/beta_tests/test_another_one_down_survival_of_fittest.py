import unittest

from katas.beta.another_one_down_survival_of_fittest import remove_smallest


class RemoveSmallestTestCase(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(remove_smallest(-10, [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_equal_2(self):
        self.assertEqual(remove_smallest(0, [1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_equal_3(self):
        self.assertEqual(remove_smallest(2, [5, 3, 2, 1, 4]), [5, 3, 4])

    def test_equal_4(self):
        self.assertEqual(remove_smallest(3, [5, 3, 2, 1, 4]), [5, 4])

    def test_equal_5(self):
        self.assertEqual(remove_smallest(3, [1, 2, 3, 4, 5]), [4, 5])

    def test_equal_6(self):
        self.assertEqual(remove_smallest(5, [1, 2, 3, 4, 5]), [])

    def test_equal_7(self):
        self.assertEqual(remove_smallest(9, [1, 2, 3, 4, 5]), [])

    def test_equal_8(self):
        self.assertEqual(remove_smallest(2, [1, 2, 1, 2, 1]), [2, 2, 1])


if __name__ == '__main__':
    unittest.main()
