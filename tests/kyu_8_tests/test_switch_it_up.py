import unittest

from katas.kyu_8.switch_it_up import switch_it_up


class SwitchItUpTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(switch_it_up(0), 'Zero')

    def test_equal_2(self):
        self.assertEqual(switch_it_up(1), 'One')

    def test_equal_3(self):
        self.assertEqual(switch_it_up(2), 'Two')

    def test_equal_4(self):
        self.assertEqual(switch_it_up(3), 'Three')

    def test_equal_5(self):
        self.assertEqual(switch_it_up(4), 'Four')

    def test_equal_6(self):
        self.assertEqual(switch_it_up(5), 'Five')

    def test_equal_7(self):
        self.assertEqual(switch_it_up(6), 'Six')

    def test_equal_8(self):
        self.assertEqual(switch_it_up(7), 'Seven')

    def test_equal_9(self):
        self.assertEqual(switch_it_up(8), 'Eight')

    def test_equal_10(self):
        self.assertEqual(switch_it_up(9), 'Nine')
