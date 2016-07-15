import unittest

from katas.kyu_7.keypad_horror import computer_to_phone


class ComputerToPhoneTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(computer_to_phone('94561'), '34567')

    def test_equals_2(self):
        self.assertEqual(computer_to_phone('000'), '000')

    def test_equals_3(self):
        self.assertEqual(computer_to_phone('0789456123'), '0123456789')
