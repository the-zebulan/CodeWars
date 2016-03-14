import unittest

from kyu_7.eighties_kids_2_help_alf_find_his_spaceship import find_spaceship


class FindSpaceshipTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_spaceship('X'), [0, 0])

    def test_equals_2(self):
        self.assertEqual(find_spaceship('X\n.'), [0, 1])

    def test_equals_3(self):
        self.assertEqual(find_spaceship('.X\n..'), [1, 1])

    def test_equals_4(self):
        self.assertEqual(find_spaceship('..\n.X'), [1, 0])

    def test_equals_5(self):
        self.assertEqual(find_spaceship('..\nX.'), [0, 0])

    def test_equals_6(self):
        self.assertEqual(find_spaceship('.......\nX.......'), [0, 0])

    def test_equals_7(self):
        self.assertEqual(find_spaceship(
            '..........\n..........\n.......X..\n..........\n..........'
        ), [7, 2])

    def test_equals_8(self):
        self.assertEqual(find_spaceship(
            '..........\n..........\n..........\n........X.\n..........'
        ), [8, 1])

    def test_equals_9(self):
        self.assertEqual(find_spaceship('........................'),
                         'Spaceship lost forever.')

    def test_equals_10(self):
        self.assertEqual(find_spaceship('\n\n\n\n'),
                         'Spaceship lost forever.')

    def test_equals_11(self):
        self.assertEqual(type(find_spaceship('X')), list)

    def test_equals_12(self):
        self.assertEqual(type(find_spaceship('')), str)


if __name__ == '__main__':
    unittest.main()
