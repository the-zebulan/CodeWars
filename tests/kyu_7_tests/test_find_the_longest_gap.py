import unittest

from kyu_7.find_the_longest_gap import gap


class GapTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(gap(9), 2)

    def test_equals_2(self):
        self.assertEqual(gap(529), 4)

    def test_equals_3(self):
        self.assertEqual(gap(20), 1)

    def test_equals_4(self):
        self.assertEqual(gap(15), 0)


if __name__ == '__main__':
    unittest.main()
