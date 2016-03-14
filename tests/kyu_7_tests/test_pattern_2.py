import unittest

from kyu_7.pattern_2 import pattern


class PatternTwoTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pattern(1), '1')

    def test_equals_2(self):
        self.assertEqual(pattern(4), '4321\n432\n43\n4')

    def test_equals_3(self):
        self.assertEqual(pattern(5), '54321\n5432\n543\n54\n5')

    def test_equals_4(self):
        self.assertEqual(pattern(10),
                         '10987654321\n1098765432\n109876543\n10987654\n'
                         '1098765\n109876\n10987\n1098\n109\n10')


if __name__ == '__main__':
    unittest.main()
