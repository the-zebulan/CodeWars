import unittest

from katas.kyu_7.frequency_sequence import freq_seq


class FrequencySequenceTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(freq_seq('hello world', '-'), '1-1-3-3-2-1-1-2-1-3-1')

    def test_equal_2(self):
        self.assertEqual(freq_seq('19999999',    ':'), '1:7:7:7:7:7:7:7')

    def test_equal_3(self):
        self.assertEqual(freq_seq('^^^**$',      'x'), '3x3x3x2x2x1')
