import unittest

from katas.beta.plus_1_array import up_array


class UpArrayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(up_array([2, 3, 9]), [2, 4, 0])

    def test_equals_2(self):
        self.assertEqual(up_array([4, 3, 2, 5]), [4, 3, 2, 6])

    def test_none(self):
        self.assertIsNone(up_array([1, -9]))

    def test_none_2(self):
        self.assertIsNone(up_array([]))


if __name__ == '__main__':
    unittest.main()
