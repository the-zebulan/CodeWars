import unittest

from beta.merge_2048 import merge


class Merge2048TestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(merge([8, 16, 16, 8]), [8, 32, 8, 0])

    def test_equals_2(self):
        self.assertEqual(merge([2, 0, 0, 0, 2]), [4, 0, 0, 0, 0])

    def test_equals_3(self):
        self.assertEqual(merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])

    def test_equals_4(self):
        self.assertEqual(merge([2, 0, 2, 2]), [4, 2, 0, 0])

    def test_equals_5(self):
        self.assertEqual(merge([2, 0, 2, 4]), [4, 4, 0, 0])

    def test_equals_6(self):
        self.assertEqual(merge([0, 0, 2, 2]), [4, 0, 0, 0])


if __name__ == '__main__':
    unittest.main()
