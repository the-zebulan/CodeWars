import unittest

from kyu_6.run_length_encoding import run_length_encoding


class RunLengthEncodingTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(run_length_encoding(
            'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb'), [[34, 'a'], [3, 'b']])

    def test_equals_2(self):
        self.assertEqual(run_length_encoding(''), [])

    def test_equals_3(self):
        self.assertEqual(run_length_encoding('abc'),
                         [[1, 'a'], [1, 'b'], [1, 'c']])

    def test_equals_4(self):
        self.assertEqual(run_length_encoding('aab'), [[2, 'a'], [1, 'b']])

    def test_equals_5(self):
        self.assertEqual(run_length_encoding('hello world!'), [
            [1, 'h'], [1, 'e'], [2, 'l'], [1, 'o'], [1, ' '], [1, 'w'],
            [1, 'o'], [1, 'r'], [1, 'l'], [1, 'd'], [1, '!']])

    def test_equals_6(self):
        self.assertEqual(run_length_encoding(
            'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb'), [[34, 'a'], [3, 'b']])

    def test_equals_7(self):
        self.assertEqual(run_length_encoding(
            'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWW'
            'WWWW'), [[12, 'W'], [1, 'B'], [12, 'W'], [3, 'B'],
                      [24, 'W'], [1, 'B'], [14, 'W']])


if __name__ == '__main__':
    unittest.main()
