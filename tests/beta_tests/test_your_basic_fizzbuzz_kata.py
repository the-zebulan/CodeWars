import unittest

from katas.beta.your_basic_fizzbuzz_kata import fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_equals_2(self):
        self.assertEqual(fizzbuzz(2), 2)

    def test_equals_3(self):
        self.assertEqual(fizzbuzz(3), 'fizz')

    def test_equals_4(self):
        self.assertEqual(fizzbuzz(4), 4)

    def test_equals_5(self):
        self.assertEqual(fizzbuzz(9), 'fizz')

    def test_equals_6(self):
        self.assertEqual(fizzbuzz(15), 'fizz buzz')

    def test_equals_7(self):
        self.assertEqual(fizzbuzz(20), 'buzz')

    def test_equals_8(self):
        self.assertEqual(fizzbuzz(25), 'buzz')

    def test_equals_9(self):
        self.assertEqual(fizzbuzz(37), 37)

    def test_equals_10(self):
        self.assertEqual(fizzbuzz(45), 'fizz buzz')


if __name__ == '__main__':
    unittest.main()
