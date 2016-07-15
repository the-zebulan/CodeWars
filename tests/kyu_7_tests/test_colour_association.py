import unittest

from katas.kyu_7.colour_association import colour_association


class ColourAssociationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(colour_association([
            ['white', 'goodness'], ['blue', 'tranquility']
        ]), [{'white': 'goodness'}, {'blue': 'tranquility'}])

    def test_equals_2(self):
        self.assertEqual(colour_association([
            ['red', 'energy'], ['yellow', 'creativity'],
            ['brown', 'friendly'], ['green', 'growth']
        ]), [{'red': 'energy'}, {'yellow': 'creativity'},
             {'brown': 'friendly'}, {'green': 'growth'}])

    def test_equals_3(self):
        self.assertEqual(colour_association([
            ['pink', 'compassion'], ['purple', 'ambition']
        ]), [{'pink': 'compassion'}, {'purple': 'ambition'}])

    def test_equals_4(self):
        self.assertEqual(colour_association([
            ['gray', 'intelligence'], ['black', 'classy']
        ]), [{'gray': 'intelligence'}, {'black': 'classy'}])

    def test_equals_5(self):
        self.assertEqual(colour_association([
            ['white', 'goodness'], ['blue', 'goodness']
        ]), [{'white': 'goodness'}, {'blue': 'goodness'}])
