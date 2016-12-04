import unittest

from katas.kyu_6.find_the_missing_letter import find_missing_letter


class FindMissingLetterTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(find_missing_letter(['a', 'b', 'c', 'd', 'f']), 'e')

    def test_equal_2(self):
        self.assertEqual(find_missing_letter(['O', 'Q', 'R', 'S']), 'P')

    def test_equal_3(self):
        self.assertEqual(find_missing_letter(['b', 'd']), 'c')
