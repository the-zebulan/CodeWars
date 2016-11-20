import unittest

from katas.beta.format_to_the_second import print_nums


class PrintNumsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(print_nums(), '')

    def test_equal_2(self):
        self.assertEqual(print_nums(2), '2')

    def test_equal_3(self):
        self.assertEqual(print_nums(1, 12, 34), '01\n12\n34')

    def test_equal_4(self):
        self.assertEqual(print_nums(1009, 2), '1009\n0002')
