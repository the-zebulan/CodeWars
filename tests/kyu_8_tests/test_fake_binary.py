import unittest

from katas.kyu_8.fake_binary import fake_bin


class FakeBinaryTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(fake_bin('45385593107843568'), '01011110001100111')

    def test_equal_2(self):
        self.assertEqual(fake_bin('509321967506747'), '101000111101101')

    def test_equal_3(self):
        self.assertEqual(fake_bin('366058562030849490134388085'),
                         '011011110000101010000011011')

    def test_equal_4(self):
        self.assertEqual(fake_bin('15889923'), '01111100')

    def test_equal_5(self):
        self.assertEqual(fake_bin('800857237867'), '100111001111')
