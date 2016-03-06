import unittest

from Kyu_7.pattern_4 import pattern


class PatternFourTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pattern(1), '1')

    def test_equals_2(self):
        self.assertEqual(pattern(2), '12\n2')

    def test_equals_3(self):
        self.assertEqual(pattern(5), '12345\n2345\n345\n45\n5')

    def test_equals_4(self):
        self.assertEqual(pattern(10),
                         '12345678910\n2345678910\n345678910\n45678910\n'
                         '5678910\n678910\n78910\n8910\n910\n10')


if __name__ == '__main__':
    unittest.main()
