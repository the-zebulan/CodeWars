import unittest

from katas.beta.assignment_2 import mirror


class MirrorTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(mirror(
            '9! xhlglUqU2mj*gfV', '1vtwf9lj!c4xk5dzsh07n=mae6/y2'
        ), 'an hxmgmuqu1l=*gey')

    def test_equal_2(self):
        self.assertEqual(mirror("Welcome home"), "dvoxlnv slnv")

    def test_equal_3(self):
        self.assertEqual(mirror("hello"), "svool")

    def test_equal_4(self):
        self.assertEqual(mirror("goodbye"), "tllwybv")

    def test_equal_5(self):
        self.assertEqual(mirror("ngmlsoor"), "mtnohlli")

    def test_equal_6(self):
        self.assertEqual(mirror("gsrh rh z hvxivg"), "this is a secret")

    def test_equal_7(self):
        self.assertEqual(mirror("Welcome home", "w"), "welcome home")

    def test_equal_8(self):
        self.assertEqual(mirror("hello", "abcdefgh"), "adllo")

    def test_equal_9(self):
        self.assertEqual(mirror("goodbye", ""), "goodbye")

    def test_equal_10(self):
        self.assertEqual(mirror("CodeWars", "+-*/="), "codewars")

    def test_equal_11(self):
        self.assertEqual(mirror("this is a secret", " *"), "this*is*a*secret")


if __name__ == '__main__':
    unittest.main()
