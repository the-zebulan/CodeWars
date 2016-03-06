import unittest

from Kyu_7.rule_of_divisibility_by_7 import seven


class SevenTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(seven(483), (42, 1))

    def test_equals_2(self):
        self.assertEqual(seven(371), (35, 1))

    def test_equals_3(self):
        self.assertEqual(seven(1603), (7, 2))

    def test_equals_4(self):
        self.assertEqual(seven(477557101), (28, 7))

    def test_equals_5(self):
        self.assertEqual(seven(0), (0, 0))


if __name__ == '__main__':
    unittest.main()
