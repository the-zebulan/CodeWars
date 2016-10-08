import unittest

from katas.kyu_7.the_office_1_outed import outed


class OutedTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(outed({
            'tim': 0, 'jim': 2, 'randy': 0, 'sandy': 7, 'andy': 0, 'katie': 5,
            'laura': 1, 'saajid': 2, 'alex': 3, 'john': 2, 'mr': 0}, 'laura'
        ), 'Get Out Now!')

    def test_equal_2(self):
        self.assertEqual(outed({
            'tim': 1, 'jim': 3, 'randy': 9, 'sandy': 6, 'andy': 7, 'katie': 6,
            'laura': 9, 'saajid': 9, 'alex': 9, 'john': 9, 'mr': 8}, 'katie'
        ), 'Nice Work Champ!')

    def test_equal_3(self):
        self.assertEqual(outed({
            'tim': 2, 'jim': 4, 'randy': 0, 'sandy': 5, 'andy': 8, 'katie': 6,
            'laura': 2, 'saajid': 2, 'alex': 3, 'john': 2, 'mr': 8}, 'john'
        ), 'Get Out Now!')

    # There is an issue with the division used in the katas Python solution
    # The following test can result in either string depending on the
    # Python version (floor division VS true division)
    # update after I get a response...

    # def test_equal_4(self):
    #     self.assertEqual(outed({
    #         'alex': 3, 'mr': 7, 'jim': 9, 'laura': 4, 'randy': 9, 'sandy': 6,
    #         'andy': 8, 'katie': 0, 'john': 4, 'tim': 0, 'saajid': 5}, 'jim'
    #     ), 'Nice Work Champ!')

    def test_equal_5(self):
        self.assertEqual(outed({
            'alex': 6, 'jim': 1, 'saajid': 9, 'laura': 5, 'tim': 4, 'randy': 0,
            'andy': 4, 'mr': 3, 'john': 1, 'sandy': 2, 'katie': 9}, 'saajid'
        ), 'Get Out Now!')

    def test_equal_6(self):
        self.assertEqual(outed({
            'alex': 3, 'jim': 7, 'saajid': 4, 'laura': 6, 'tim': 8, 'randy': 7,
            'andy': 8, 'mr': 9, 'john': 3, 'sandy': 0, 'katie': 1}, 'sandy'
        ), 'Get Out Now!')
