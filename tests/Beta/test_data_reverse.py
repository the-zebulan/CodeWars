import unittest

from Beta.data_reverse import data_reverse


class DataReverseTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(data_reverse(
            [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]),
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1,
             0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1])

    def test_equals_2(self):
        self.assertEqual(data_reverse(
            [0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]),
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
