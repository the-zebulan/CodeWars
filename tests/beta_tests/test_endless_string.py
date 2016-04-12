import unittest

from katas.beta.endless_string import endlessString


class EndlessStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(endlessString('xyz', -23, 6), 'yzxyzx')

    def test_equals_2(self):
        self.assertEqual(endlessString('xyz', 0, 4), 'xyzx')

    def test_equals_3(self):
        self.assertEqual(endlessString('xyz', 19, 2), 'yz')

    def test_equals_4(self):
        self.assertEqual(endlessString('xyz', -4, -4), 'zxyz')

    def test_equals_5(self):
        self.assertEqual(endlessString('1x2x3x4x', -1532, -100),
                         'x2x3x4x1x2x3x4x1x2x3x4x1x2x3x4x1x2x3x4x1x2x3x4x1x2'
                         'x3x4x1x2x3x4x1x2x3x4x1x2x3x4x1x2x3x4x1x2x3x4x1x2x3')


if __name__ == '__main__':
    unittest.main()
