import unittest

from katas.kyu_7.fizz_buzz import fizzbuzz


class FizzBuzzTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(fizzbuzz(10), [
            1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz'
        ])


if __name__ == '__main__':
    unittest.main()
