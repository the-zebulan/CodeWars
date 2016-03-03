import unittest

from Beta.multiples import multiple


class MultiplesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(multiple(30), 'BangBoom')

    def test_equals_2(self):
        self.assertEqual(multiple(3), 'Bang')

    def test_equals_3(self):
        self.assertEqual(multiple(98), 'Miss')

    def test_equals_4(self):
        self.assertEqual(multiple(65), 'Boom')

    def test_equals_5(self):
        self.assertEqual(multiple(23), 'Miss')

    def test_equals_6(self):
        self.assertEqual(multiple(15), 'BangBoom')


if __name__ == '__main__':
    unittest.main()
