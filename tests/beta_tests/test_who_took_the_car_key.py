import unittest

from katas.beta.who_took_the_car_key import who_took_the_car_key


class WhoTookTheCarKeyTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(who_took_the_car_key(
            ['01000001', '01101100', '01100101', '01111000', '01100001',
             '01101110', '01100100', '01100101', '01110010']
        ), 'Alexander')

    def test_equal_2(self):
        self.assertEqual(who_took_the_car_key(
            ['01001010', '01100101', '01110010', '01100101', '01101101',
             '01111001']
        ), 'Jeremy')

    def test_equal_3(self):
        self.assertEqual(who_took_the_car_key(
            ['01000011', '01101000', '01110010', '01101001', '01110011']
        ), 'Chris')

    def test_equal_4(self):
        self.assertEqual(who_took_the_car_key(
            ['01001010', '01100101', '01110011', '01110011', '01101001',
             '01100011', '01100001']
        ), 'Jessica')

    def test_equal_5(self):
        self.assertEqual(who_took_the_car_key(
            ['01001010', '01100101', '01110010', '01100101', '01101101',
             '01111001']
        ), 'Jeremy')
