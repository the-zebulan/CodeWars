import unittest

from katas.kyu_6.dashatize_it import dashatize


class DashatizeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(dashatize(274), '2-7-4')

    def test_equal_2(self):
        self.assertEqual(dashatize(5311), '5-3-1-1')

    def test_equal_3(self):
        self.assertEqual(dashatize(86320), '86-3-20')

    def test_equal_4(self):
        self.assertEqual(dashatize(974302), '9-7-4-3-02')

    def test_equal_5(self):
        self.assertEqual(dashatize(None), 'None')

    def test_equal_6(self):
        self.assertEqual(dashatize(0), '0')

    def test_equal_7(self):
        self.assertEqual(dashatize(-1), '1')

    def test_equal_8(self):
        self.assertEqual(dashatize(-28369), '28-3-6-9')
