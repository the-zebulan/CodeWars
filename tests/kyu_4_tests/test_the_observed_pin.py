import unittest

from katas.kyu_4.the_observed_pin import get_pins


class ObservedPinTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_pins('8'), sorted('57890'))

    def test_equal_2(self):
        self.assertEqual(get_pins('11'), sorted([
            '11', '22', '44', '12', '21', '14', '41', '24', '42'
        ]))

    def test_equal_3(self):
        self.assertEqual(get_pins('369'), sorted([
            '339', '366', '399', '658', '636', '258', '268', '669', '668',
            '266', '369', '398', '256', '296', '259', '368', '638', '396',
            '238', '356', '659', '639', '666', '359', '336', '299', '338',
            '696', '269', '358', '656', '698', '699', '298', '236', '239'
        ]))


if __name__ == '__main__':
    unittest.main()
