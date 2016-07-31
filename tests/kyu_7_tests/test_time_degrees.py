import unittest

from katas.kyu_7.time_degrees import clock_degree


class ClockDegreeTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(clock_degree('00:00'), '360:360')

    def test_equal_2(self):
        self.assertEqual(clock_degree('01:01'), '30:6')

    def test_equal_3(self):
        self.assertEqual(clock_degree('00:01'), '360:6')

    def test_equal_4(self):
        self.assertEqual(clock_degree('01:00'), '30:360')

    def test_equal_5(self):
        self.assertEqual(clock_degree('01:30'), '30:180')

    def test_equal_6(self):
        self.assertEqual(clock_degree('24:00'), 'Check your time !')

    def test_equal_7(self):
        self.assertEqual(clock_degree('13:60'), 'Check your time !')

    def test_equal_8(self):
        self.assertEqual(clock_degree('20:34'), '240:204')

    def test_equal_9(self):
        self.assertEqual(clock_degree('01:03'), '30:18')

    def test_equal_10(self):
        self.assertEqual(clock_degree('12:05'), '360:30')

    def test_equal_11(self):
        self.assertEqual(clock_degree('26:78'), 'Check your time !')

    def test_equal_12(self):
        self.assertEqual(clock_degree('16:25'), '120:150')

    def test_equal_13(self):
        self.assertEqual(clock_degree('17:09'), '150:54')

    def test_equal_14(self):
        self.assertEqual(clock_degree('19:00'), '210:360')

    def test_equal_15(self):
        self.assertEqual(clock_degree('23:20'), '330:120')

    def test_equal_16(self):
        self.assertEqual(clock_degree('-09:00'), 'Check your time !')
