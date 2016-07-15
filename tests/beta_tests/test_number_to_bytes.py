import unittest

from katas.beta.number_to_bytes import to_bytes


class NumberToBytesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(to_bytes(0), ['00000000'])

    def test_equals_2(self):
        self.assertEqual(to_bytes(1), ['00000001'])

    def test_equals_3(self):
        self.assertEqual(to_bytes(257), ['00000001', '00000001'])

    def test_equals_4(self):
        self.assertEqual(to_bytes(0x101), ['00000001', '00000001'])

    def test_equals_5(self):
        self.assertEqual(to_bytes(0x000000000101), ['00000001', '00000001'])

    def test_equals_6(self):
        self.assertEqual(to_bytes(0xffff), ['11111111', '11111111'])

    def test_equals_7(self):
        self.assertEqual(to_bytes(0x1020304),
                         ['00000001', '00000010', '00000011', '00000100'])
