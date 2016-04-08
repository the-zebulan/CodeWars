import unittest

from katas.beta.what_color_is_your_name import stringColor


class StringColorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(stringColor('Jack'), '7A90E5')

    def test_equals_2(self):
        self.assertEqual(stringColor('Joshua'), '6C0FD7')

    def test_equals_3(self):
        self.assertEqual(stringColor('Joshua Smith'), '935AFE')

    def test_equals_4(self):
        self.assertEqual(stringColor('Hayden Smith'), '82F0F1')

    def test_equals_5(self):
        self.assertEqual(stringColor('Mathew Smith'), '8F00F4')


if __name__ == '__main__':
    unittest.main()
