import unittest

from katas.kyu_8.multiply_the_number import multiply


class MultiplyTheNumberTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(multiply(10), 250)

    def test_equals_2(self):
        self.assertEqual(multiply(5), 25)

    def test_equals_3(self):
        self.assertEqual(multiply(200), 25000)

    def test_equals_4(self):
        self.assertEqual(multiply(0), 0)

    def test_equals_5(self):
        self.assertEqual(multiply(-2), -10)


if __name__ == '__main__':
    unittest.main()
