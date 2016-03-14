import unittest

from katas.kyu_7.debug_basic_calculator import calculate


class CalculateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(calculate(6, "-", 1.5), 4.5)

    def test_equals_2(self):
        self.assertEqual(calculate(-4, "*", 8), -32)

    def test_none(self):
        self.assertIsNone(calculate(8, "m", 2))

    def test_none_2(self):
        self.assertIsNone(calculate(4, "/", 0))


if __name__ == '__main__':
    unittest.main()
