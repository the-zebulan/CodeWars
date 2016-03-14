import unittest

from kyu_4.strings_mix import mix


class MixTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(mix('my&friend&Paul has heavy hats! &',
                             'my friend John has many many friends &'),
                         '2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:'
                         'rr/=:ee/=:ss')

    def test_equals_2(self):
        self.assertEqual(mix(
            'mmmmm m nnnnn y&friend&Paul has heavy hats! &',
            'my frie n d Joh n has ma n y ma n y frie n ds n&'),
            '1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/='
            ':ss')

    def test_equals_3(self):
        self.assertEqual(mix('Are the kids at home? aaaaa fffff',
                             'Yes they are here! aaaaa fffff'),
                         '=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh')

    def test_equals_4(self):
        self.assertEqual(mix('Are they here', 'yes, they are here'),
                         '2:eeeee/2:yy/=:hh/=:rr')

    def test_equals_5(self):
        self.assertEqual(mix('looping is fun but dangerous',
                             'less dangerous than coding'),
                         '1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg')

    def test_equals_6(self):
        self.assertEqual(mix(' In many languages',
                             ' there\'s a pair of functions'),
                         '1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt')

    def test_equals_7(self):
        self.assertEqual(mix('Lords of the Fallen', 'gamekult'),
                         '1:ee/1:ll/1:oo')

    def test_equals_8(self):
        self.assertEqual(mix('codewars', 'codewars'), '')

    def test_equals_9(self):
        self.assertEqual(mix('A generation must confront the looming ',
                             'codewarrs'),
                         '1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr')


if __name__ == '__main__':
    unittest.main()
