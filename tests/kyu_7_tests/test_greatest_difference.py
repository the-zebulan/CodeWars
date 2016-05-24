import unittest

from katas.kyu_7.greatest_difference import diff


class GreatestDifferenceTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(diff(['56-23', '1-100']), '1-100')

    def test_equal_2(self):
        self.assertEqual(diff(['1-3', '5-7', '2-3']), '1-3')

    def test_equal_3(self):
        self.assertEqual(diff([
            '36-43', '3-3', '66-66', '19-19', '539-539', '5--831', '721-770',
            '6--55', '943-945', '9-9'
        ]), '5--831')

    def test_equal_4(self):
        self.assertEqual(diff([
            '62-646', '255--623', '5-942', '683-683', '30-30', '9-9', '10-10',
            '22-267', '53-53', '262-262', '27-27', '541-541', '97-168',
            '12-12'
        ]), '5-942')

    def test_equal_5(self):
        self.assertEqual(diff([
            '57--275', '689-756', '9--9', '168-481', '872-872', '571-604',
            '652-1149', '113-119', '5-10', '44--53', '755-1063', '8--455',
            '908-908', '8-323', '4-4', '10-28', '12--317', '1--30'
        ]), '652-1149')

    def test_equal_6(self):
        self.assertEqual(diff([
            '799-627', '49-20', '354-1168', '8-8', '47-39', '2-12', '17-17',
            '52--27', '568-470', '7--378', '625-625', '4-4', '34-89'
        ]), '354-1168')

    def test_equal_7(self):
        self.assertEqual(diff([
            '38-10', '61-61', '10-10', '646-643', '2-2', '148-148', '28-28',
            '71-71', '856-876', '8--764', '9--105', '20--54'
        ]), '8--764')

    def test_equal_8(self):
        self.assertEqual(diff([
            '63-63', '79-84', '694-694', '82-784', '2-2', '7--907', '964-970',
            '856-612', '56--3', '8--210', '6-662', '98-254'
        ]), '7--907')

    def test_equal_9(self):
        self.assertEqual(diff([
            '9-9', '50--200', '4--169', '8-8', '155-1117', '504-504', '2-12',
            '347--345', '6-6', '88-88', '4--365', '2-2', '960-1213',
            '71--697', '66-66'
        ]), '155-1117')

    def test_equal_10(self):
        self.assertEqual(diff([
            '585-189', '88-88', '41-41', '2-275', '315-315'
        ]), '585-189')

    def test_equal_11(self):
        self.assertEqual(diff(['12--268', '10-10', '3-3', '722-722', '7-7']),
                         '12--268')

    def test_equal_12(self):
        self.assertEqual(diff([
            '7-574', '34-34', '33-9', '716-716', '688-1062', '73--207'
        ]), '7-574')

    def test_false_1(self):
        self.assertFalse(diff(['11-11', '344-344']))


if __name__ == '__main__':
    unittest.main()
