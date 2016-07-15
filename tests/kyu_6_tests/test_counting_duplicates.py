import unittest

from katas.kyu_6.counting_duplicates import duplicate_count


class DuplicateCountTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(duplicate_count("abcde"), 0)

    def test_equals_2(self):
        self.assertEqual(duplicate_count("abcdea"), 1)

    def test_equals_3(self):
        self.assertEqual(duplicate_count("aabbcde"), 2)

    def test_equals_4(self):
        self.assertEqual(duplicate_count("aabbcdeB"), 2)

    def test_equals_5(self):
        self.assertEqual(duplicate_count("indivisibility"), 1)

    def test_equals_6(self):
        self.assertEqual(duplicate_count('indivisibilities'), 2)
