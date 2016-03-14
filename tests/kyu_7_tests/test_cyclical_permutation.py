import unittest

from katas.kyu_7.cyclical_permutation import pattern


class CyclicalPermutationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(pattern(1), '1')

    def test_equals_2(self):
        self.assertEqual(pattern(4), '1234\n2341\n3412\n4123')

    def test_equals_3(self):
        self.assertEqual(pattern(10),
                         '12345678910\n23456789101\n34567891012\n45678910123'
                         '\n56789101234\n67891012345\n78910123456\n891012345'
                         '67\n91012345678\n10123456789')


if __name__ == '__main__':
    unittest.main()
