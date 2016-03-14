import unittest

from katas.beta.unscrambled_eggs import unscramble_eggs


class UnscrambleEggsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(unscramble_eggs('Beggegeggineggneggeregg'), 'Beginner')

    def test_equals_2(self):
        self.assertEqual(unscramble_eggs('ceggodegge heggeregge'), 'code here')

    def test_equals_3(self):
        self.assertEqual(unscramble_eggs('FeggUNegg KeggATeggA'), 'FUN KATA')


if __name__ == '__main__':
    unittest.main()
