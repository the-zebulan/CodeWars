import unittest

from katas.kyu_7.holiday_v_seasick_snorkelling import sea_sick


class SeaSickTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sea_sick('~'), 'No Problem')

    def test_equal_2(self):
        self.assertEqual(sea_sick('_~~~~~~~_~__~______~~__~~_~~'), 'Throw Up')

    def test_equal_3(self):
        self.assertEqual(sea_sick('______~___~_'), 'Throw Up')

    def test_equal_4(self):
        self.assertEqual(sea_sick('____'), 'No Problem')

    def test_equal_5(self):
        self.assertEqual(sea_sick('_~~_~____~~~~~~~__~_~'), 'Throw Up')
