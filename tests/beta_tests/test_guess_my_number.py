import unittest

from katas.beta.guess_my_number import guess_my_number


class GuessMyNumberTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(guess_my_number('0'), '###-###-####')

    def test_equals_2(self):
        self.assertEqual(guess_my_number('01'), '1##-##1-####')

    def test_equals_3(self):
        self.assertEqual(guess_my_number('012'), '12#-##1-2###')

    def test_equals_4(self):
        self.assertEqual(guess_my_number('0123'), '123-##1-23##')

    def test_equals_5(self):
        self.assertEqual(guess_my_number('01234'), '123-4#1-234#')

    def test_equals_6(self):
        self.assertEqual(guess_my_number('012345'), '123-451-2345')


if __name__ == '__main__':
    unittest.main()
