import unittest

from kyu_6.square_n_sum import square_sum


class SquareSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(square_sum([1, 2]), 5)

    def test_equals_2(self):
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)


if __name__ == '__main__':
    unittest.main()
