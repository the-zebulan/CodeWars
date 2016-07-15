import unittest

from katas.beta.valid_hk_phone_number import \
    has_valid_HK_phone_number, is_valid_HK_phone_number


class ValidHKPhoneNumberTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(is_valid_HK_phone_number('1234 5678'))

    def test_true_2(self):
        self.assertTrue(is_valid_HK_phone_number('2359 1478'))

    def test_true_3(self):
        self.assertTrue(is_valid_HK_phone_number('9684 2396'))

    def test_true_4(self):
        self.assertTrue(is_valid_HK_phone_number('0000 0000'))

    def test_true_5(self):
        self.assertTrue(has_valid_HK_phone_number(
            'Hello, my phone number is 1234 5678'
        ))

    def test_true_6(self):
        self.assertTrue(has_valid_HK_phone_number(
            'I wonder if 2359 1478 is a valid phone number?'
        ))

    def test_true_7(self):
        self.assertTrue(has_valid_HK_phone_number('     1234 5678   '))

    def test_true_8(self):
        self.assertTrue(has_valid_HK_phone_number('What about 9684 2396?'))

    def test_true_9(self):
        self.assertTrue(has_valid_HK_phone_number(
            'skldfjsdklfjs0000 0000skldfjslkdfjs'
        ))

    def test_false_1(self):
        self.assertFalse(is_valid_HK_phone_number('85748475'))

    def test_false_2(self):
        self.assertFalse(is_valid_HK_phone_number('3857  4756'))

    def test_false_3(self):
        self.assertFalse(is_valid_HK_phone_number('sklfjsdklfjsf'))

    def test_false_4(self):
        self.assertFalse(is_valid_HK_phone_number('     1234 5678   '))

    def test_false_5(self):
        self.assertFalse(is_valid_HK_phone_number('abcd efgh'))

    def test_false_6(self):
        self.assertFalse(is_valid_HK_phone_number('836g 2986'))

    def test_false_7(self):
        self.assertFalse(is_valid_HK_phone_number('123456789'))

    def test_false_8(self):
        self.assertFalse(is_valid_HK_phone_number(' 987 634 '))

    def test_false_9(self):
        self.assertFalse(is_valid_HK_phone_number('    6    '))

    def test_false_10(self):
        self.assertFalse(is_valid_HK_phone_number('8A65 2986'))

    def test_false_11(self):
        self.assertFalse(is_valid_HK_phone_number('8368 2aE6'))

    def test_false_12(self):
        self.assertFalse(is_valid_HK_phone_number('8c65 2i86'))

    def test_false_13(self):
        self.assertFalse(has_valid_HK_phone_number(
            '85748475 is definitely invalid'
        ))

    def test_false_14(self):
        self.assertFalse(has_valid_HK_phone_number(
            "'3857  4756' is so close to a valid phone number!"
        ))

    def test_false_15(self):
        self.assertFalse(has_valid_HK_phone_number('sklfjsdklfjsf'))

    def test_false_16(self):
        self.assertFalse(has_valid_HK_phone_number('What about abcd efgh?'))

    def test_false_17(self):
        self.assertFalse(has_valid_HK_phone_number('And 836g 2986?'))

    def test_false_18(self):
        self.assertFalse(has_valid_HK_phone_number('123456789 is invalid'))

    def test_false_19(self):
        self.assertFalse(has_valid_HK_phone_number(
            'sdfssdfsdfdf 987 634 sdfsddsds'
        ))

    def test_false_20(self):
        self.assertFalse(has_valid_HK_phone_number('\n\n    6    \n\n'))

    def test_false_21(self):
        self.assertFalse(has_valid_HK_phone_number(
            'sdfsdsdfdf8A65 2986sdfsddfs'
        ))

    def test_false_22(self):
        self.assertFalse(has_valid_HK_phone_number('iwoeurwoeuwo8368 2aE6'))

    def test_false_23(self):
        self.assertFalse(has_valid_HK_phone_number(
            '8c65 2i86wioeruwioeruweoi'
        ))
