import unittest

from beta.multiples_2 import multiples


class MultiplesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(multiples(49), 'Fizz')

    def test_equals_2(self):
        self.assertEqual(multiples(147), 'Fang')

    def test_equals_3(self):
        self.assertEqual(multiples(30), 'Foo')

    def test_equals_4(self):
        self.assertEqual(multiples(51), 'Far')


if __name__ == '__main__':
    unittest.main()
