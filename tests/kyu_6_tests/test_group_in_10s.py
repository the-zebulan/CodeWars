import unittest

from katas.kyu_6.group_in_10s import group_in_10s


class GroupInTensTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(group_in_10s(1, 2, 3), [[1, 2, 3]])

    def test_equals_2(self):
        self.assertEqual(group_in_10s(8, 12, 38, 3, 17, 19, 25, 35, 50),
                         [[3, 8], [12, 17, 19], [25], [35, 38], None, [50]])

    def test_equals_3(self):
        self.assertEqual(group_in_10s(12, 10, 11, 13, 25, 28, 29, 49, 51, 90),
                         [None, [10, 11, 12, 13], [25, 28, 29], None,
                          [49], [51], None, None, None, [90]])

    def test_equals_4(self):
        self.assertEqual(group_in_10s(), [])

    def test_equals_5(self):
        self.assertEqual(group_in_10s(100), [
            None, None, None, None, None, None, None, None, None, None, [100]])


if __name__ == '__main__':
    unittest.main()
