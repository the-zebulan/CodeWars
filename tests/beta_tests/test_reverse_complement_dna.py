import unittest

from katas.beta.reverse_complement_dna import reverse_complement


class ReverseComplementTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(reverse_complement('TTCCGGAA'), 'TTCCGGAA')

    def test_equal_2(self):
        self.assertEqual(reverse_complement('GACTGACTGTA'), 'TACAGTCAGTC')

    def test_equal_3(self):
        self.assertEqual(reverse_complement(''), '')

    def test_equal_4(self):
        self.assertEqual(reverse_complement('XYZ'), 'Invalid sequence')


if __name__ == '__main__':
    unittest.main()
