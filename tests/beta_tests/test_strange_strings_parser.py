import unittest

from katas.beta.strange_strings_parser import parser


class ParserTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(parser('12:56C:144:1000:1200'),
                         ['12', '56C', '144', '1000', '1200'])

    def test_equal_2(self):
        self.assertEqual(parser('23;RPM;300;PSI;MODE;FORWARD'),
                         ['23', 'RPM', '300', 'PSI', 'MODE', 'FORWARD'])

    def test_equal_3(self):
        self.assertEqual(
            parser('340000.00*-140.49902*ELEVATION*24000000*END'),
            ['340000.00', '-140.49902', 'ELEVATION', '24000000', 'END'])
