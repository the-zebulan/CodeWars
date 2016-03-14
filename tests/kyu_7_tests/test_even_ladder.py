import unittest

from Kyu_7.even_ladder import pattern


class EvenLadderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pattern(8), '22\n4444\n666666\n88888888')

    def test_equals_2(self):
        self.assertEqual(pattern(5), '22\n4444')


if __name__ == '__main__':
    unittest.main()
