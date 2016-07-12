import unittest

from katas.kyu_8.collatz_conjecture import hotpo


class CollatzConjectureTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(hotpo(1), 0)

    def test_equal_2(self):
        self.assertEqual(hotpo(5), 5)

    def test_equal_3(self):
        self.assertEqual(hotpo(6), 8)

    def test_equal_4(self):
        self.assertEqual(hotpo(23), 15)


if __name__ == '__main__':
    unittest.main()
