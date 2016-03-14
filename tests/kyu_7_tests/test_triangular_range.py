import unittest

from kyu_7.triangular_range import triangular_range


class TriangularRangeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(triangular_range(1, 3), {1: 1, 2: 3})

    def test_equals_2(self):
        self.assertEqual(triangular_range(5, 16), {3: 6, 4: 10, 5: 15})


if __name__ == '__main__':
    unittest.main()
