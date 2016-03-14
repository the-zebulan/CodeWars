import unittest

from katas.kyu_6.binary_to_text_conversion import binary_to_string


class BinaryToStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(binary_to_string(
            '0100100001100101011011000110110001101111'), 'Hello')

    def test_equals_2(self):
        self.assertEqual(binary_to_string(
            '00110001001100000011000100110001'), '1011')


if __name__ == '__main__':
    unittest.main()
