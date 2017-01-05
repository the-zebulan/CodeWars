import unittest

from katas.kyu_6.street_fighter_2_character_selection import (
    street_fighter_selection)


class StreetFighterSelectionTestCase(unittest.TestCase):
    def setUp(self):
        self.fighters = [
            ['Ryu', 'E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega'],
            ['Ken', 'Chun Li', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison']]

    def test_equal_1(self):
        self.assertEqual(street_fighter_selection(
            self.fighters, (0, 0), []), [])

    def test_equal_2(self):
        self.assertEqual(street_fighter_selection(
            self.fighters, (0, 0), ['left'] * 8),
            ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega',
             'Balrog'])

    def test_equal_3(self):
        self.assertEqual(street_fighter_selection(
            self.fighters, (0, 0), ['right'] * 8),
            ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda',
             'Blanka'])

    def test_equal_4(self):
        self.assertEqual(street_fighter_selection(
            self.fighters, (0, 0), ['up'] * 4),
            ['Ryu', 'Ryu', 'Ryu', 'Ryu'])

    def test_equal_5(self):
        self.assertEqual(street_fighter_selection(
            self.fighters, (0, 0), ['down'] * 4),
            ['Ken', 'Ken', 'Ken', 'Ken'])

    def test_equal_6(self):
        self.assertEqual(street_fighter_selection(
            self.fighters, (0, 0), ['down', 'right', 'up', 'left'] * 2),
            ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda',
             'Ryu'])

    def test_equal_7(self):
        self.assertEqual(street_fighter_selection(
            self.fighters, (0, 0), ['up', 'left', 'down', 'right'] * 2),
            ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken'])

    def test_equal_8(self):
        self.assertEqual(street_fighter_selection(
            self.fighters, (0, 0),
            ['up'] + ['left'] * 6 + ['down'] + ['right'] * 6),
            ['Ryu', 'Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu',
             'Ken', 'Chun Li', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison',
             'Ken'])
