import unittest

from kyu_7.length_of_line_segment import length_of_line


class LengthOfLineTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(length_of_line([[0, 0], [1, 1]]), '1.41')

    def test_equals_2(self):
        self.assertEqual(length_of_line([[0, 0], [-5, -6]]), '7.81')

    def test_equals_3(self):
        self.assertEqual(length_of_line([[0, 0], [10, 15]]), '18.03')

    def test_equals_4(self):
        self.assertEqual(length_of_line([[0, 0], [5, 1]]), '5.10')

    def test_equals_5(self):
        self.assertEqual(length_of_line([[0, 0], [5, 4]]), '6.40')

    def test_equals_6(self):
        self.assertEqual(length_of_line([[0, 0], [-7, 4]]), '8.06')

    def test_equals_7(self):
        self.assertEqual(length_of_line([[0, 0], [0, 0]]), '0.00')

    def test_equals_8(self):
        self.assertEqual(length_of_line([[-3, 4], [10, 5]]), '13.04')


if __name__ == '__main__':
    unittest.main()
