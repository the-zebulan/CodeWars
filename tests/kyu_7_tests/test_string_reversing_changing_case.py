import unittest

from katas.kyu_7.string_reversing_changing_case import reverse_and_mirror


class ReverseAndMirrorTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(reverse_and_mirror('FizZ', 'buZZ'),
                         'zzUB@@@zZIffIZz')

    def test_equal_2(self):
        self.assertEqual(reverse_and_mirror(
            'String Reversing', 'Changing Case'),
            'ESAc GNIGNAHc@@@GNISREVEr GNIRTssTRING rEVERSING')
