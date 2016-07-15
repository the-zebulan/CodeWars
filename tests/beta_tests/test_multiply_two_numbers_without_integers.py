import unittest

from katas.beta.multiply_two_numbers_without_integers import multiplyMyNumbers


class MultiplyTwoNumberWithoutIntegersTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(multiplyMyNumbers('1', '5'), '5')

    def test_equals_2(self):
        self.assertEqual(multiplyMyNumbers('7', '2'), '14')

    def test_equals_3(self):
        self.assertEqual(multiplyMyNumbers('11', '42'), '462')

    def test_equals_4(self):
        self.assertEqual(multiplyMyNumbers('12', '35'), '420')

    def test_equals_5(self):
        self.assertEqual(multiplyMyNumbers('00000012', '00000035'), '420')

    def test_equals_6(self):
        self.assertEqual(multiplyMyNumbers('12345' * 10, '00000002'),
                         '24690246902469024690246902469024690246902469024690')
