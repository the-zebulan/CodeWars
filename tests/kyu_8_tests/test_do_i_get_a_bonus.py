import unittest

from katas.kyu_8.do_i_get_a_bonus import bonus_time


class BonusTimeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(bonus_time(10000, True), '$100000')

    def test_equals_2(self):
        self.assertEqual(bonus_time(25000, True), '$250000')

    def test_equals_3(self):
        self.assertEqual(bonus_time(10000, False), '$10000')

    def test_equals_4(self):
        self.assertEqual(bonus_time(60000, False), '$60000')

    def test_equals_5(self):
        self.assertEqual(bonus_time(2, True), '$20')

    def test_equals_6(self):
        self.assertEqual(bonus_time(78, False), '$78')

    def test_equals_7(self):
        self.assertEqual(bonus_time(67890, True), '$678900')
