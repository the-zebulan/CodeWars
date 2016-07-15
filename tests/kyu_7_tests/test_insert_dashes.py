import unittest

from katas.kyu_7.insert_dashes import insert_dash


class InsertDashTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(insert_dash(454793), '4547-9-3')

    def test_equals_2(self):
        self.assertEqual(insert_dash(123456), '123456')

    def test_equals_3(self):
        self.assertEqual(insert_dash(1003567), '1003-567')

    def test_equals_4(self):
        self.assertEqual(insert_dash(24680), '24680')

    def test_equals_5(self):
        self.assertEqual(insert_dash(13579), '1-3-5-7-9')
