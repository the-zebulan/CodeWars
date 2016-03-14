import unittest

from beta.summations_1 import summation


class SummationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(summation(10), 55)

    def test_equals_2(self):
        self.assertEqual(summation(5), 15)

    def test_equals_3(self):
        self.assertEqual(summation('538'), 'Error 404')

    def test_equals_4(self):
        self.assertEqual(summation(67.9), 'Error 404')


if __name__ == '__main__':
    unittest.main()
