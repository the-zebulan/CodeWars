import unittest

from Kyu_6.duplicate_encoder import duplicate_encode


class DuplicateEncoderTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(duplicate_encode('din'), '(((')

    def test_equals_2(self):
        self.assertEqual(duplicate_encode('recede'), '()()()')

    def test_equals_3(self):
        self.assertEqual(duplicate_encode('Success'), ')())())')

    def test_equals_4(self):
        self.assertEqual(duplicate_encode('(( @'), '))((')


if __name__ == '__main__':
    unittest.main()
