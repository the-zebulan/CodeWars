import unittest

from katas.kyu_7.coding_3_min_to_lover_case import to_lover_case


class ToLoverCaseTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(to_lover_case('LOVE'), 'EVOL')

    def test_equal_2(self):
        self.assertEqual(to_lover_case('love'), 'EVOL')

    def test_equal_3(self):
        self.assertEqual(to_lover_case('abcd'), 'LOVE')

    def test_equal_4(self):
        self.assertEqual(to_lover_case('ebcd'), 'LOVE')

    def test_equal_5(self):
        self.assertEqual(to_lover_case('Hello World!'), 'ELEEV VVOEE!')

    def test_equal_6(self):
        self.assertEqual(to_lover_case('jrvz,'), 'OOOO,')


if __name__ == '__main__':
    unittest.main()
