import unittest

from kyu_8.string_to_number import string_to_number


class StringToNumberTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(string_to_number('1234'), 1234)

    def test_equals_2(self):
        self.assertEqual(string_to_number('605'), 605)

    def test_equals_3(self):
        self.assertEqual(string_to_number('1405'), 1405)

    def test_equals_4(self):
        self.assertEqual(string_to_number('1234'), 1234)


if __name__ == '__main__':
    unittest.main()
