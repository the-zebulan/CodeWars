import unittest

from katas.beta.sort_the_columns_of_a_csv_file import sort_csv_columns


class SortCSVColumnsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sort_csv_columns(
            'myjinxin2015;raulbc777;smile67;Dentzil;SteffenVogel_79\n'
            '17945;10091;10088;3907;10132\n'
            '2;12;13;48;11'),
            'Dentzil;myjinxin2015;raulbc777;smile67;SteffenVogel_79\n'
            '3907;17945;10091;10088;10132\n'
            '48;2;12;13;11')

    def test_equal_2(self):
        self.assertEqual(sort_csv_columns(
            'Captain America;Hulk;IronMan;Thor\n'
            'honorably;angry;arrogant;divine\n'
            'shield;greenhorn;armor;hammer\n'
            'Steven;Bruce;Tony;Thor'),
            'Captain America;Hulk;IronMan;Thor\n'
            'honorably;angry;arrogant;divine\n'
            'shield;greenhorn;armor;hammer\n'
            'Steven;Bruce;Tony;Thor')
