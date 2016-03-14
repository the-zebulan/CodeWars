import unittest

from kyu_8.regex_count_lowercase_letters import lowercase_count


class LowercaseCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(lowercase_count('abc'), 3)

    def test_equals_2(self):
        self.assertEqual(lowercase_count('abcABC123'), 3)

    def test_equals_3(self):
        self.assertEqual(lowercase_count(
            'abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~'), 3)

    def test_equals_4(self):
        self.assertEqual(lowercase_count(''), 0)

    def test_equals_5(self):
        self.assertEqual(lowercase_count(
            'ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~'), 0)

    def test_equals_6(self):
        self.assertEqual(lowercase_count('abcdefghijklmnopqrstuvwxyz'), 26)


if __name__ == '__main__':
    unittest.main()
