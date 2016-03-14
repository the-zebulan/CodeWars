import unittest

from katas.kyu_6.polybius_square_cipher_encode import polybius


class PolybiusTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(polybius('CODEWARS'), '1334141552114243')

    def test_equals_2(self):
        self.assertEqual(polybius('POLYBIUS SQUARE CIPHER'),
                         '3534315412244543 434145114215 132435231542')


if __name__ == '__main__':
    unittest.main()
