import unittest

from beta.multi_range_iterator import multiiter


class MultiIterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(list(multiiter(0)), [])

    def test_equals_2(self):
        self.assertEqual(list(multiiter(2)), [(0,), (1,)])

    def test_equals_3(self):
        self.assertEqual(list(multiiter(2, 3)), [(0, 0), (0, 1), (0, 2),
                                                 (1, 0), (1, 1), (1, 2)])

    def test_equals_4(self):
        self.assertEqual(list(multiiter(3, 2)), [(0, 0), (0, 1), (1, 0),
                                                 (1, 1), (2, 0), (2, 1)])


if __name__ == '__main__':
    unittest.main()
