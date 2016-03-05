import unittest

from Kyu_6.stop_spinning_my_words import spin_words


class SpinWordsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(spin_words('Welcome'), 'emocleW')

    def test_equals_2(self):
        self.assertEqual(spin_words('Hey fellow warriors'),
                         'Hey wollef sroirraw')

    def test_equals_3(self):
        self.assertEqual(spin_words('This is a test'), 'This is a test')

    def test_equals_4(self):
        self.assertEqual(spin_words('This is another test'),
                         'This is rehtona test')


if __name__ == '__main__':
    unittest.main()
