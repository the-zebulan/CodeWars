import unittest

from Kyu_7.penultimate import penultimate


class PenultimateTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(penultimate([1, 2, 3, 4]), 3)

    def test_equals_2(self):
        self.assertEqual(penultimate([1, 2, 3, 4, 5, 6, 7]), 6)


if __name__ == '__main__':
    unittest.main()
