import unittest

from katas.beta.hollow_triangle import hollow_Triangle


class HollowTriangleTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(hollow_Triangle(1), ['#'])

    def test_equal_2(self):
        self.assertEqual(hollow_Triangle(2), [
            '_#_',
            '###'
        ])

    def test_equal_3(self):
        self.assertEqual(hollow_Triangle(3), [
            '__#__',
            '_#_#_',
            '#####'
        ])

    def test_equal_4(self):
        self.assertEqual(hollow_Triangle(4), [
            '___#___',
            '__#_#__',
            '_#___#_',
            '#######'
        ])

    def test_equal_5(self):
        self.assertEqual(hollow_Triangle(6), [
            '_____#_____',
            '____#_#____',
            '___#___#___',
            '__#_____#__',
            '_#_______#_',
            '###########'
        ])

    def test_equal_6(self):
        self.assertEqual(hollow_Triangle(9), [
            '________#________',
            '_______#_#_______',
            '______#___#______',
            '_____#_____#_____',
            '____#_______#____',
            '___#_________#___',
            '__#___________#__',
            '_#_____________#_',
            '#################'
        ])


if __name__ == '__main__':
    unittest.main()
