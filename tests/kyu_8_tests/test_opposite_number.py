import unittest

from katas.kyu_8.opposite_number import opposite


class OppositeNumberTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(opposite(1), -1)

    def test_equals_2(self):
        self.assertEqual(opposite(25.6), -25.6)

    def test_equals_3(self):
        self.assertEqual(opposite(0), 0)

    def test_equals_4(self):
        self.assertEqual(opposite(1425.2222), -1425.2222)

    def test_equals_5(self):
        self.assertEqual(opposite(-3.1458), 3.1458)

    def test_equals_6(self):
        self.assertEqual(opposite(-95858588225), 95858588225)

if __name__ == '__main__':
    unittest.main()
