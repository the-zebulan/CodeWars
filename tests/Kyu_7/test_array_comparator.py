import unittest

from Kyu_7.array_comparator import match_arrays


class MatchArraysTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(match_arrays(
            ['Perl', 'Closure', 'JavaScript'], ['Go', 'C++', 'Erlang']), 0)

    def test_equals_2(self):
        self.assertEqual(match_arrays(
            ['Erlang', 'JavaScript'], ['Go', 'C++', 'Python']), 0)

    def test_equals_3(self):
        self.assertEqual(match_arrays(
            [True, 3, 9, 11, 15], [True, 3, 11]), 3)


if __name__ == '__main__':
    unittest.main()
