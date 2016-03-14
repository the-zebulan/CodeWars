import unittest

from Beta.anagram_or_not import isAnagram


class IsAnagramTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(isAnagram(
            'William Shakespeare', 'I am a weakish speller'))

    def test_true_2(self):
        self.assertTrue(isAnagram('Silent', 'Listen'))

    def test_true_3(self):
        self.assertTrue(isAnagram('12345', '54321'))

    def test_false(self):
        self.assertFalse(isAnagram('Car', 'Cat'))


if __name__ == '__main__':
    unittest.main()
