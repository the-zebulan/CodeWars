import unittest

from katas.kyu_7.number_of_occurrences import number_of_occurrences


class NumberOfOccurrencesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(number_of_occurrences(4, []), 0)

    def test_equals_2(self):
        self.assertEqual(number_of_occurrences(4, [4, 0, 4]), 2)

    def test_equals_3(self):
        self.assertEqual(number_of_occurrences(
            1024, [1024, 1024, 2056, 512, 256, 4096, 1024]
        ), 3)

    def test_equals_4(self):
        self.assertEqual(number_of_occurrences(
            9, [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ), 1)

    def test_equals_5(self):
        self.assertEqual(number_of_occurrences(
            'abc', ['abc', '123', '123', 'abc']
        ), 2)


if __name__ == '__main__':
    unittest.main()
