import unittest

from katas.beta.number_star_ladder import pattern


class PatternTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pattern(3), '1\n1*2\n1**3')

    def test_equals_2(self):
        self.assertEqual(pattern(7),
                         '1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7')

    def test_equals_3(self):
        self.assertEqual(pattern(20),
                         '1\n1*2\n1**3\n1***4\n1****5\n1*****6\n1******7\n'
                         '1*******8\n1********9\n1*********10\n1**********11\n'
                         '1***********12\n1************13\n1*************14\n'
                         '1**************15\n1***************16\n'
                         '1****************17\n1*****************18\n'
                         '1******************19\n1*******************20')


if __name__ == '__main__':
    unittest.main()
