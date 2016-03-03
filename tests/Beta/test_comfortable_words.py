import unittest

from Beta.comfortable_words import comfortable_word


class ComfortableWordTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(comfortable_word('yams'))

    def test_false(self):
        self.assertFalse(comfortable_word('test'))


if __name__ == '__main__':
    unittest.main()
