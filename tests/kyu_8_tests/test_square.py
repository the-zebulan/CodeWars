import unittest

from kyu_8.square import square


class SquareTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(square(2), 4)

    def test_equals_2(self):
        self.assertEqual(square(50), 2500)

    def test_equals_3(self):
        self.assertEqual(square(1), 1)


if __name__ == '__main__':
    unittest.main()
