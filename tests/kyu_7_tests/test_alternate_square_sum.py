import unittest

from kyu_7.alternate_square_sum import alternate_sq_sum


class AlternateSquareSumTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(alternate_sq_sum([11, 12, 13, 14, 15]), 379)

    def test_equals_2(self):
        self.assertEqual(alternate_sq_sum([11, 5, 6, 11, 11, 8, 8, 13]), 415)

    def test_equals_3(self):
        self.assertEqual(alternate_sq_sum(
            [5, 15, 9, 12, 13, 16, 13, 7, 5, 7, 7, 15, 8, 6, 13]), 1057)

    def test_equals_4(self):
        self.assertEqual(alternate_sq_sum([16, 10, 9, 12, 7, 11, 9, 8]), 470)

    def test_equals_5(self):
        self.assertEqual(alternate_sq_sum([5, 8, 15, 6, 12, 8, 10]), 206)

    def test_equals_6(self):
        self.assertEqual(alternate_sq_sum(
            [7, 15, 16, 15, 16, 12, 5, 10, 6, 6, 13, 14]), 989)

    def test_equals_7(self):
        self.assertEqual(alternate_sq_sum(
            [13, 10, 11, 15, 9, 6, 6, 14, 7, 5, 6, 13, 14]), 817)

    def test_equals_8(self):
        self.assertEqual(alternate_sq_sum(
            [15, 10, 8, 10, 6, 7, 8, 8, 13, 14, 13, 8, 6]), 642)

    def test_equals_9(self):
        self.assertEqual(alternate_sq_sum(
            [8, 5, 10, 13, 10, 6, 8, 5, 7, 9]), 379)

    def test_equals_10(self):
        self.assertEqual(alternate_sq_sum(
            [11, 5, 13, 6, 8, 14, 7, 7, 15, 16, 7, 9, 9, 15, 11, 7]), 998)

    def test_equals_11(self):
        self.assertEqual(alternate_sq_sum([11, 8, 14, 5, 7, 15]), 346)


if __name__ == '__main__':
    unittest.main()
