import unittest

from katas.kyu_7.coding_3min_bug_in_apple import sc


class BugInAppleTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sc([
            ['B', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A']
        ]), [0, 0])

    def test_equals_2(self):
        self.assertEqual(sc([
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'B', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A']
        ]), [1, 1])

    def test_equals_3(self):
        self.assertEqual(sc([
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'A', 'A', 'A', 'A'],
            ['A', 'B', 'A', 'A', 'A']
        ]), [4, 1])


if __name__ == '__main__':
    unittest.main()
