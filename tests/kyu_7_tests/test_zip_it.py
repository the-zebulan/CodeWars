import unittest

from kyu_7.zip_it import lstzip


class ZipItTestCase(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2, 3, 4, 5]
        self.b = ['a', 'b', 'c', 'd', 'e']

    def test_equals(self):
        self.assertEqual(lstzip(self.a, self.b, lambda c, d: str(c) + str(d)),
                         ['1a', '2b', '3c', '4d', '5e'])

    def test_equals_2(self):
        self.assertEqual(lstzip(self.b, self.a, lambda e, f: str(e) + str(f)),
                         ['a1', 'b2', 'c3', 'd4', 'e5'])

    def test_equals_3(self):
        self.assertEqual(lstzip(self.b, lstzip(
            self.a, self.b, lambda g, h: g * ord(h[0])),
                                lambda i, j: str(i) + str(j)),
                         ['a97', 'b196', 'c297', 'd400', 'e505'])


if __name__ == '__main__':
    unittest.main()
