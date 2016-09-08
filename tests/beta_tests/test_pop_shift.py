import unittest

from katas.beta.pop_shift import pop_shift


class PopShiftTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(
            pop_shift('reusetestcasesbitcointakeovertheworldmaybewhoknowspe'
                      'rhaps'),
            ['spahrepswonkohwebyamdlroweht', 'reusetestcasesbitcointakeove',
             'r']
        )

    def test_equal_2(self):
        self.assertEqual(
            pop_shift('turnsoutrandomtestcasesareeasierthanwritingoutbasico'
                      'nes'),
            ['senocisabtuognitirwnahtreis','turnsoutrandomtestcasesaree', 'a']
        )

    def test_equal_3(self):
        self.assertEqual(pop_shift('letstalkaboutjavascriptthebestlanguage'),
                         ['egaugnaltsebehttpir', 'letstalkaboutjavasc', ''])

    def test_equal_4(self):
        self.assertEqual(pop_shift('exampletesthere'),
                         ['erehtse', 'example', 't'])

    def test_equal_5(self):
        self.assertEqual(pop_shift('iwanttotraveltheworldwritingcodeoneday'),
                         ['yadenoedocgnitirwdl', 'iwanttotravelthewor', ''])

    def test_equal_6(self):
        self.assertEqual(pop_shift('letsallgoonholidaysomewhereverycold'),
                         ['dlocyreverehwemos', 'letsallgoonholida', 'y'])
