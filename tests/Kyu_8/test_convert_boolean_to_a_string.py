import unittest

from Kyu_8.convert_boolean_to_a_string import boolean_to_string


class BooleanToStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(boolean_to_string(True), 'True')

    def test_equals_2(self):
        self.assertEqual(boolean_to_string(False), 'False')


if __name__ == '__main__':
    unittest.main()
