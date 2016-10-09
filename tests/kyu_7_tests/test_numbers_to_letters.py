import unittest

from katas.kyu_7.numbers_to_letters import switcher


class SwitcherTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(switcher([
            '24', '12', '23', '22', '4', '26', '9', '8']), 'codewars')

    def test_equal_2(self):
        self.assertEqual(switcher([
            '25', '7', '8', '0', '4', '14', '23', '8', '25', '23', '29', '16',
            '16', '4']), 'btswmdsbd kkw')

    def test_equal_3(self):
        self.assertEqual(switcher([
            '12', '28', '25', '21', '25', '7', '11', '22', '0', '15']),
            'o?bfbtpel')

    def test_equal_4(self):
        self.assertEqual(switcher(['4', '24']), 'wc')

    def test_equal_5(self):
        self.assertEqual(switcher(['12']), 'o')
