import unittest

from katas.kyu_6.rainfall import mean, variance


class RainfallTestCase(unittest.TestCase):
    def setUp(self):
        self.test = 'Rome:Jan 81.2,Feb 63.2,Mar 70.3,Apr 55.7,May 53.0,Jun ' \
                    '36.4,Jul 17.5,Aug 27.5,Sep 60.9,Oct 117.7,Nov 111.0,De' \
                    'c 97.9\nLondon:Jan 48.0,Feb 38.9,Mar 39.9,Apr 42.2,May' \
                    ' 47.3,Jun 52.1,Jul 59.5,Aug 57.2,Sep 55.4,Oct 62.0,Nov' \
                    ' 59.0,Dec 52.9\nParis:Jan 182.3,Feb 120.6,Mar 158.1,Ap' \
                    'r 204.9,May 323.1,Jun 300.5,Jul 236.8,Aug 192.9,Sep 66' \
                    '.3,Oct 63.3,Nov 83.2,Dec 154.7\nNY:Jan 108.7,Feb 101.8' \
                    ',Mar 131.9,Apr 93.5,May 98.8,Jun 93.6,Jul 102.2,Aug 13' \
                    '1.8,Sep 92.0,Oct 82.3,Nov 107.8,Dec 94.2\nVancouver:Ja' \
                    'n 145.7,Feb 121.4,Mar 102.3,Apr 69.2,May 55.8,Jun 47.1' \
                    ',Jul 31.3,Aug 37.0,Sep 59.6,Oct 116.3,Nov 154.6,Dec 17' \
                    '1.5\nSydney:Jan 103.4,Feb 111.0,Mar 131.3,Apr 129.7,Ma' \
                    'y 123.0,Jun 129.2,Jul 102.8,Aug 80.3,Sep 69.3,Oct 82.6' \
                    ',Nov 81.4,Dec 78.2\nBangkok:Jan 10.6,Feb 28.2,Mar 30.7' \
                    ',Apr 71.8,May 189.4,Jun 151.7,Jul 158.2,Aug 187.0,Sep ' \
                    '319.9,Oct 230.8,Nov 57.3,Dec 9.4\nTokyo:Jan 49.9,Feb 7' \
                    '1.5,Mar 106.4,Apr 129.2,May 144.0,Jun 176.0,Jul 135.6,' \
                    'Aug 148.5,Sep 216.4,Oct 194.1,Nov 95.6,Dec 54.4\nBeiji' \
                    'ng:Jan 3.9,Feb 4.7,Mar 8.2,Apr 18.4,May 33.0,Jun 78.1,' \
                    'Jul 224.3,Aug 170.0,Sep 58.4,Oct 18.0,Nov 9.3,Dec 2.7' \
                    '\nLima:Jan 1.2,Feb 0.9,Mar 0.7,Apr 0.4,May 0.6,Jun 1.8' \
                    ',Jul 4.4,Aug 3.1,Sep 3.3,Oct 1.7,Nov 0.5,Dec 0.7'

    def test_equals(self):
        self.assertEqual(round(mean('London', self.test)), 51.0)

    def test_equals_2(self):
        self.assertEqual(round(mean('Beijing', self.test)), 52.0)

    def test_equals_3(self):
        self.assertEqual(round(variance('London', self.test)), 57.0)

    def test_equals_4(self):
        self.assertEqual(round(variance('Beijing', self.test)), 4808.0)

    def test_equals_5(self):
        self.assertEqual(mean('Zimbabwe', self.test), -1)

    def test_equals_6(self):
        self.assertEqual(variance('Sundre', self.test), -1)


if __name__ == '__main__':
    unittest.main()
