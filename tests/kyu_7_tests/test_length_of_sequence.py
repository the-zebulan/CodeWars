import unittest

from Kyu_7.length_of_sequence import length_of_sequence


class LengthOfSequenceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(length_of_sequence([1, 1], 1), 2)

    def test_equals_2(self):
        self.assertEqual(length_of_sequence([1, 2, 3, 1], 1), 4)

    def test_equals_3(self):
        self.assertEqual(length_of_sequence([-7, 5, 0, 2, 9, 5], 10), 0)

    def test_equals_4(self):
        self.assertEqual(length_of_sequence([-7, 5, 0, 2, 9, 5], 5), 5)

    def test_equals_5(self):
        self.assertEqual(length_of_sequence([1, 2, 3, 1, 2, 3, 1], 1), 0)


if __name__ == '__main__':
    unittest.main()
