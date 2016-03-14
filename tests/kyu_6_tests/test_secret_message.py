import unittest

from kyu_6.secret_message import find_secret_message


class FindSecretMessageTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_secret_message(
            'thing sleeps is in, HAVE, always? in thing out is: WANTS a! goo'
            'd T-Rex, is, never, sleeps good NEVER, chocolate? Think the in '
            'Is THING? thing: Pippi? sleeps T-Rex'),
            'in thing is sleeps good never t-rex')

    def test_equals_2(self):
        self.assertEqual(find_secret_message(
            'This is a test. this test is fun.'), 'this test is')

    def test_equals_3(self):
        self.assertEqual(find_secret_message(
            'asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. qwer crfv.'),
            'zxcv asdf qwer')


if __name__ == '__main__':
    unittest.main()
