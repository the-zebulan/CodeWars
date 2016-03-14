import unittest

from Kyu_8.regexp_basics_is_it_a_digit import is_digit


class IsDigitTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_digit("7"))

    def test_false(self):
        self.assertFalse(is_digit(""))

    def test_false_2(self):
        self.assertFalse(is_digit(" "))

    def test_false_3(self):
        self.assertFalse(is_digit("a"))

    def test_false_4(self):
        self.assertFalse(is_digit("a5"))


if __name__ == '__main__':
    unittest.main()
