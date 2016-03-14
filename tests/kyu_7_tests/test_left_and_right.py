import unittest

from Kyu_7.left_and_right import left, right


class TestCase(unittest.TestCase):
    def setUp(self):
        self.text = 'Hello (not so) cruel World!'

    def test_equals(self):
        self.assertEqual(left(self.text, 5), 'Hello')

    def test_equals_2(self):
        self.assertEqual(left(self.text, -22), 'Hello')

    def test_equals_3(self):
        self.assertEqual(left(self.text, 1), 'H')

    def test_equals_4(self):
        self.assertEqual(left(self.text), 'H')

    def test_equals_5(self):
        self.assertEqual(left(self.text, 0), '')

    def test_equals_6(self):
        self.assertEqual(left(self.text, 99), 'Hello (not so) cruel World!')

    def test_equals_7(self):
        self.assertEqual(right(self.text, 6), 'World!')

    def test_equals_8(self):
        self.assertEqual(right(self.text), '!')

    def test_equals_9(self):
        self.assertEqual(left(self.text, 'o'), 'Hell')

    def test_equals_10(self):
        self.assertEqual(right(self.text, 'o'), 'rld!')

    def test_equals_11(self):
        self.assertEqual(left(self.text, ' '), 'Hello')

    def test_equals_12(self):
        self.assertEqual(right("Don't Repeat Yourself", 'Repeat '), 'Yourself')


if __name__ == '__main__':
    unittest.main()
