import unittest

from katas.kyu_7.noobcode_4_hot_singles import hot_singles


class HotSinglesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(hot_singles(
            ['tartar', 'blanket', 'domino'], ['blanket']
        ), ['tartar', 'domino'])

    def test_equal_2(self):
        self.assertEqual(hot_singles(
            [77, 'basketweave'], [78, 42, 'basketweave']
        ), [77, 78, 42])

    def test_equal_3(self):
        self.assertEqual(hot_singles(
            [100, 45, 'ciao'], [100, 2, 3, 45, 5]
        ), ['ciao', 2, 3, 5])

    def test_equal_4(self):
        self.assertEqual(hot_singles(
            [10, 200, 30], [10, 20, 3, 4, 5, 5, 5, 200]
        ), [30, 20, 3, 4, 5])

    def test_equal_5(self):
        self.assertEqual(hot_singles(
            [1, 2, 3, 3], [3, 2, 1, 4, 5, 4]
        ), [4, 5])


if __name__ == '__main__':
    unittest.main()
