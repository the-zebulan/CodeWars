import unittest

from katas.kyu_7.parallelogram import pattern


class ParallelogramTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pattern(3), '  123\n 123 \n123  ')

    def test_equals_2(self):
        self.assertEqual(
            pattern(5), '    12345\n   12345 \n  12345  \n 12345   \n12345    '
        )

    def test_equals_3(self):
        self.assertEqual(
            pattern(8), '       12345678\n      12345678 \n     12345678  \n'
                        '    12345678   \n   12345678    \n  12345678     \n'
                        ' 12345678      \n12345678       '
        )


if __name__ == '__main__':
    unittest.main()
