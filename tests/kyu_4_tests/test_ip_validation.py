import unittest

from katas.kyu_4.ip_validation import is_valid_IP


class IPValidationTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_valid_IP('12.255.56.1'))

    def test_false(self):
        self.assertFalse(is_valid_IP(''))

    def test_false_2(self):
        self.assertFalse(is_valid_IP('abc.def.ghi.jkl'))

    def test_false_3(self):
        self.assertFalse(is_valid_IP('123.456.789.0'))

    def test_false_4(self):
        self.assertFalse(is_valid_IP('12.34.56'))

    def test_false_5(self):
        self.assertFalse(is_valid_IP('12.34.56 .1'))

    def test_false_6(self):
        self.assertFalse(is_valid_IP('12.34.56.-1'))

    def test_false_7(self):
        self.assertFalse(is_valid_IP('123.045.067.089'))


if __name__ == '__main__':
    unittest.main()
