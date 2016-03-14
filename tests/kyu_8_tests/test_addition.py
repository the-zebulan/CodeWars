import unittest

from kyu_8.addition import on_square, total_after


class AdditionTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(on_square(10), 512)

    def test_equals_2(self):
        self.assertEqual(on_square(7), 64)

    def test_equals_3(self):
        self.assertEqual(total_after(25), 33554431)

    def test_equals_4(self):
        self.assertEqual(total_after(37), 137438953471)


if __name__ == '__main__':
    unittest.main()
