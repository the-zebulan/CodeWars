import unittest

from kyu_6.ipv4_to_int32 import ip_to_int32


class IPToInt32TestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(ip_to_int32('128.114.17.104'), 2154959208)

    def test_equals_2(self):
        self.assertEqual(ip_to_int32('0.0.0.0'), 0)

    def test_equals_3(self):
        self.assertEqual(ip_to_int32('128.32.10.1'), 2149583361)


if __name__ == '__main__':
    unittest.main()
