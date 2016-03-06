import unittest

from Kyu_7.credit_card_mask import maskify


class MaskifyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(maskify('4556364607935616'), '############5616')

    def test_equals_2(self):
        self.assertEqual(maskify('64607935616'), '#######5616')

    def test_equals_3(self):
        self.assertEqual(maskify('1'), '1')

    def test_equals_4(self):
        self.assertEqual(maskify(''), '')


if __name__ == '__main__':
    unittest.main()
