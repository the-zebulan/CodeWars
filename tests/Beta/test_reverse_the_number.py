import unittest

from Beta.reverse_the_number import reverse


class ReverseTheNumberTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(reverse(123456), 654321)

    def test_equals_2(self):
        self.assertEqual(reverse(0), 0)

    def test_equals_3(self):
        self.assertEqual(reverse(100), 1)

    def test_equals_4(self):
        self.assertEqual(reverse(1234567891011), 1101987654321)


if __name__ == '__main__':
    unittest.main()
