import unittest

from Kyu_6.regexp_basics_is_it_ipv4_address import ipv4_address


class IPV4AddressTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(ipv4_address('127.0.0.1'))

    def test_true_2(self):
        self.assertTrue(ipv4_address('0.0.0.0'))

    def test_true_3(self):
        self.assertTrue(ipv4_address('255.255.255.255'))

    def test_true_4(self):
        self.assertTrue(ipv4_address('10.20.30.40'))

    def test_false(self):
        self.assertFalse(ipv4_address(''))

    def test_false_2(self):
        self.assertFalse(ipv4_address('10.256.30.40'))

    def test_false_3(self):
        self.assertFalse(ipv4_address('10.20.030.40'))

    def test_false_4(self):
        self.assertFalse(ipv4_address('127.0.1'))

    def test_false_5(self):
        self.assertFalse(ipv4_address('127.0.0.0.1'))

    def test_false_6(self):
        self.assertFalse(ipv4_address('..255.255'))

    def test_false_7(self):
        self.assertFalse(ipv4_address('127.0.0.1\n'))

    def test_false_8(self):
        self.assertFalse(ipv4_address('\n127.0.0.1'))

    def test_false_9(self):
        self.assertFalse(ipv4_address(' 127.0.0.1'))

    def test_false_10(self):
        self.assertFalse(ipv4_address('127.0.0.1 '))

    def test_false_11(self):
        self.assertFalse(ipv4_address(' 127.0.0.1 '))


if __name__ == '__main__':
    unittest.main()
