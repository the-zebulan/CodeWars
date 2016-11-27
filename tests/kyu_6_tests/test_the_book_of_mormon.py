import unittest

from katas.kyu_6.the_book_of_mormon import mormons


class MormonsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(mormons(10, 3, 9), 0)

    def test_equal_2(self):
        self.assertEqual(mormons(99, 2, 99), 0)

    def test_equal_3(self):
        self.assertEqual(mormons(40, 2, 120), 1)

    def test_equal_4(self):
        self.assertEqual(mormons(40, 2, 121), 2)

    def test_equal_5(self):
        self.assertEqual(mormons(20000, 2, 7000000000), 12)
