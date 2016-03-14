import unittest

from Kyu_7.is_valid_identifier import is_valid


class IsValidIdentifierTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_valid("okay_ok1"))

    def test_true_2(self):
        self.assertTrue(is_valid("$ok"))

    def test_true_3(self):
        self.assertTrue(is_valid("___"))

    def test_true_4(self):
        self.assertTrue(is_valid("str_STR"))

    def test_true_5(self):
        self.assertTrue(is_valid("myIdentf"))

    def test_false(self):
        self.assertFalse(is_valid("1ok0okay"))

    def test_false_2(self):
        self.assertFalse(is_valid("!Ok"))

    def test_false_3(self):
        self.assertFalse(is_valid(""))

    def test_false_4(self):
        self.assertFalse(is_valid("str-str"))

    def test_false_5(self):
        self.assertFalse(is_valid("no no"))


if __name__ == '__main__':
    unittest.main()
