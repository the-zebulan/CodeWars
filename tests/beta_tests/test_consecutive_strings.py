import unittest

from katas.beta.consecutive_strings import longest_consec


class ConsecutiveTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(longest_consec(
            ['zone', 'abigail', 'theta', 'form', 'libe', 'zas'], 2),
            'abigailtheta')

    def test_equals_2(self):
        self.assertEqual(longest_consec(
            ['ejjjjmmtthh', 'zxxuueeg', 'aanlljrrrxx', 'dqqqaaabbb',
             'oocccffuucccjjjkkkjyyyeehh'], 1), 'oocccffuucccjjjkkkjyyyeehh')

    def test_equals_3(self):
        self.assertEqual(longest_consec([], 3), '')

    def test_equals_4(self):
        self.assertEqual(longest_consec(
            ['itvayloxrp', 'wkppqsztdkmvcuwvereiupccauycnjutlv',
             'vweqilsfytihvrzlaodfixoyxvyuyvgpck'], 2),
            'wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfix'
            'oyxvyuyvgpck')

    def test_equals_5(self):
        self.assertEqual(longest_consec(
            ['wlwsasphmxx', 'owiaxujylentrklctozmymu', 'wpgozvxxiu'], 2),
            'wlwsasphmxxowiaxujylentrklctozmymu')

    def test_equals_6(self):
        self.assertEqual(longest_consec(
            ['zone', 'abigail', 'theta', 'form', 'libe', 'zas'], -2), '')

    def test_equals_7(self):
        self.assertEqual(longest_consec(
            ['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 3),
            'ixoyx3452zzzzzzzzzzzz')

    def test_equals_8(self):
        self.assertEqual(longest_consec(
            ['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 15), '')

    def test_equals_9(self):
        self.assertEqual(longest_consec(
            ['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 0), '')


if __name__ == '__main__':
    unittest.main()
