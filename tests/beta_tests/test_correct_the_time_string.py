import unittest

from katas.beta.correct_the_time_string import time_correct


class TimeCorrectTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(time_correct(''), '')

    def test_equal_2(self):
        self.assertEqual(time_correct('09:10:01'), '09:10:01')

    def test_equal_3(self):
        self.assertEqual(time_correct('11:70:10'), '12:10:10')

    def test_equal_4(self):
        self.assertEqual(time_correct('19:99:99'), '20:40:39')

    def test_equal_5(self):
        self.assertEqual(time_correct('24:01:01'), '00:01:01')

    def test_equal_6(self):
        self.assertEqual(time_correct('52:01:01'), '04:01:01')

    def test_is_none_1(self):
        self.assertIsNone(time_correct(None))

    def test_is_none_2(self):
        self.assertIsNone(time_correct('001122'))

    def test_is_none_3(self):
        self.assertIsNone(time_correct('00;11;22'))

    def test_is_none_4(self):
        self.assertIsNone(time_correct('0a:1c:22'))
