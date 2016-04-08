import unittest

from katas.beta.hail_caesar import hail_caesar


class CountingStarTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(hail_caesar(
            'GUR DHVPX OEBJA QBT WHZCRQ BIRE GUR YNML SBK.'
        ), 'THE QUICK BROWN DOG JUMPED OVER THE LAZY FOX.')

    def test_equals_2(self):
        self.assertEqual(hail_caesar('CODEWARS'), 'PBQRJNEF')

    def test_equals_3(self):
        self.assertEqual(hail_caesar('PBQRJNEF'), 'CODEWARS')

    def test_equals_4(self):
        self.assertEqual(hail_caesar('CAESAR'), 'PNRFNE')

    def test_equals_5(self):
        self.assertEqual(hail_caesar('PNRFNE'), 'CAESAR')

    def test_equals_6(self):
        self.assertEqual(hail_caesar('ROT13'), 'EBG13')

    def test_equals_7(self):
        self.assertEqual(hail_caesar('EBG13'), 'ROT13')


if __name__ == '__main__':
    unittest.main()
