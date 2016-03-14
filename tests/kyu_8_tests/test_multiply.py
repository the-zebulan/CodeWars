import unittest

from Kyu_8.multiply import multiply


class MultiplyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_equals_2(self):
        self.assertEqual(multiply(10, 10), 100)


if __name__ == '__main__':
    unittest.main()
