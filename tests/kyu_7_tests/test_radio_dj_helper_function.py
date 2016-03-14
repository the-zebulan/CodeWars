import unittest

from katas.kyu_7.radio_dj_helper_function import longest_possible


class LongestPossibleTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(longest_possible(215), 'For Reasons Unknown')

    def test_equals_2(self):
        self.assertEqual(longest_possible(270), 'YYZ')

    def test_false(self):
        self.assertFalse(longest_possible(13))


if __name__ == '__main__':
    unittest.main()
