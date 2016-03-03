import unittest

from Beta.dumbphone_keypads import sequence


class SequenceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sequence('HELLO WORLD'), '4433555p555666096667775553')

    def test_equals_2(self):
        self.assertEqual(sequence('codewar rocks'),
                         '2226663p33927770777666222557777')

    def test_equals_3(self):
        self.assertEqual(sequence('#hashtag'), '#442777744824')


if __name__ == '__main__':
    unittest.main()
