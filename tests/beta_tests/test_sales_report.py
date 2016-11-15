import unittest
from textwrap import dedent

from katas.beta.sales_report import generate_report


class GenerateReportTestCase(unittest.TestCase):
    def setUp(self):
        self.records = (
            ('0001', '001', 12),
            ('0012', '001', 1000),
            ('0012', '001', 32),
            ('0027', '007', 207),
            ('0112', '007', 12119),
            ('1009', '007', 200)
        )

    def test_equal_1(self):
        self.assertEqual(generate_report([]),
                         'Total:                               0')

    def test_equal_2(self):
        self.assertEqual(generate_report(self.records[:1]), dedent('''\
            Group: 001
                Product: 0001 Value:     12
                Group total:                    12

            Total:                              12'''))

    def test_equal_3(self):
        self.assertEqual(generate_report(self.records[:2]), dedent('''\
            Group: 001
                Product: 0001 Value:     12
                Product: 0012 Value:   1000
                Group total:                  1012

            Total:                            1012'''))

    def test_equal_4(self):
        self.assertEqual(generate_report(self.records), dedent('''\
            Group: 001
                Product: 0001 Value:     12
                Product: 0012 Value:   1032
                Group total:                  1044

            Group: 007
                Product: 0027 Value:    207
                Product: 0112 Value:  12119
                Product: 1009 Value:    200
                Group total:                 12526

            Total:                           13570'''))
