import unittest

from kyu_8.return_negative import make_negative


class MakeNegativeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(make_negative(42), -42)

    def test_equals_2(self):
        self.assertEqual(make_negative(-9), -9)

    def test_equals_3(self):
        self.assertEqual(make_negative(0), 0)


if __name__ == '__main__':
    unittest.main()
