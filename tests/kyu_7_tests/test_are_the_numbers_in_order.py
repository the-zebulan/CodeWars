import unittest

from kyu_7.are_the_numbers_in_order import in_asc_order


class AscendingOrderTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(in_asc_order([1, 2]))

    def test_true_2(self):
        self.assertTrue(in_asc_order([1, 2, 3]))

    def test_true_3(self):
        self.assertTrue(in_asc_order([1, 4, 13, 97, 508, 1047, 20058]))

    def test_false(self):
        self.assertFalse(in_asc_order([2, 1]))

    def test_false_2(self):
        self.assertFalse(in_asc_order([1, 3, 2]))

    def test_false_3(self):
        self.assertFalse(in_asc_order(
            [56, 98, 123, 67, 742, 1024, 32, 90969]))


if __name__ == '__main__':
    unittest.main()
