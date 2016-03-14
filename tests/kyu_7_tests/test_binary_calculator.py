import unittest

from kyu_7.binary_calculator import calculate


class CalculateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(calculate('1', '1', 'add'), '10')

    def test_equals_2(self):
        self.assertEqual(calculate('1', '1', 'subtract'), '0')

    def test_equals_3(self):
        self.assertEqual(calculate('1', '1', 'multiply'), '1')


if __name__ == '__main__':
    unittest.main()
