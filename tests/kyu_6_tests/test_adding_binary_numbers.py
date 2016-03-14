import unittest

from kyu_6.adding_binary_numbers import add


class AddingBinaryNumbersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(add('111', '10'), '1001')

    def test_equals_2(self):
        self.assertEqual(add('1101', '101'), '10010')

    def test_equals_3(self):
        self.assertEqual(add('1101', '10111'), '100100')

    def test_equals_4(self):
        self.assertEqual(add('10111', '001010101'), '1101100')

    def test_equals_5(self):
        self.assertEqual(add('00', '0'), '0')


if __name__ == '__main__':
    unittest.main()
