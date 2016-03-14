import unittest

from kyu_7.uvb76_message_validator import validate


class MessageValidatorTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(validate('MDZHB 85 596 KLASA 81 00 02 91'))

    def test_true_2(self):
        self.assertTrue(validate('MDZHB 12 733 EDINENIE 67 79 66 32'))

    def test_false(self):
        self.assertFalse(validate('Is this a right message?'))

    def test_false_2(self):
        self.assertFalse(validate('MDZHV 60 130 VATRUKH 58 89 54 54'))


if __name__ == '__main__':
    unittest.main()
