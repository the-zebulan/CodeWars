import unittest

from kyu_7.anagram_detection import is_anagram


class IsAnagramTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_anagram('Creative', 'Reactive'))

    def test_true_2(self):
        self.assertTrue(is_anagram('foefet', 'toffee'))

    def test_true_3(self):
        self.assertTrue(is_anagram('Buckethead', 'DeathCubeK'))


if __name__ == '__main__':
    unittest.main()
