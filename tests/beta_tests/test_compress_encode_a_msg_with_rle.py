import unittest

from katas.beta.compress_encode_a_msg_with_rle import encode


class EncodeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(encode('HIIITTTTHEERRRR'), 'H1I3T4H1E2R4')

    def test_equal_2(self):
        self.assertEqual(encode('RRRREEHTTTTIIIH'), 'R4E2H1T4I3H1')
