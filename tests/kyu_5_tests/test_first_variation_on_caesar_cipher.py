import unittest

from kyu_5.first_variation_on_caesar_cipher import demoving_shift, moving_shift


class CaesarCipherTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(demoving_shift(
            ['J vltasl rlhr ', 'zdfog odxr ypw', ' atasl rlhr p ',
             'gwkzzyq zntyhv', ' lvz wp!!!'], 1),
            'I should have known that you would have a perfect answer for me'
            '!!!')

    def test_equals_2(self):
        self.assertEqual(moving_shift(
            'I should have known that you would have a perfect answer for me'
            '!!!', 1),
            ['J vltasl rlhr ', 'zdfog odxr ypw', ' atasl rlhr p ',
             'gwkzzyq zntyhv', ' lvz wp!!!'])


if __name__ == '__main__':
    unittest.main()
