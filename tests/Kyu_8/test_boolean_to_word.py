import unittest

from Kyu_8.boolean_to_word import bool_to_word


class BooleanToWordTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(bool_to_word(True), 'YES')

    def test_equals_2(self):
        self.assertEqual(bool_to_word(False), 'NO')


if __name__ == '__main__':
    unittest.main()
