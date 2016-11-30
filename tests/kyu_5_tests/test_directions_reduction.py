import unittest

from katas.kyu_5.directions_reduction import dir_reduc


class DirectionsReductionTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(dir_reduc(
            ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'WEST']),
            ['WEST'])

    def test_equal_2(self):
        self.assertEqual(dir_reduc(['NORTH', 'WEST', 'SOUTH', 'EAST']),
                         ['NORTH', 'WEST', 'SOUTH', 'EAST'])

    def test_equal_3(self):
        self.assertEqual(dir_reduc(
            ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH',
             'NORTH', 'WEST', 'EAST']),
            ['NORTH', 'NORTH'])

    def test_equal_4(self):
        self.assertEqual(dir_reduc(
            ['NORTH', 'SOUTH', 'SOUTH', 'EAST', 'WEST', 'NORTH']), [])
