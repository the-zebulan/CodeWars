import unittest

from kyu_7.satisfying_numbers import smallest


class SatisfyingNumbersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(smallest(1), 1)

    def test_equals_2(self):
        self.assertEqual(smallest(2), 2)

    def test_equals_3(self):
        self.assertEqual(smallest(3), 6)

    def test_equals_4(self):
        self.assertEqual(smallest(4), 12)

    def test_equals_5(self):
        self.assertEqual(smallest(5), 60)

    def test_equals_6(self):
        self.assertEqual(smallest(6), 60)

    def test_equals_7(self):
        self.assertEqual(smallest(7), 420)

    def test_equals_8(self):
        self.assertEqual(smallest(8), 840)

    def test_equals_9(self):
        self.assertEqual(smallest(9), 2520)

    def test_equals_10(self):
        self.assertEqual(smallest(10), 2520)


if __name__ == '__main__':
    unittest.main()
