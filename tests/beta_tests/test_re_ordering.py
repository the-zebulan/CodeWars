import unittest

from katas.beta.re_ordering import re_ordering


class ReOrderingTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(re_ordering('ming Yao'), 'Yao ming')

    def test_equal_2(self):
        self.assertEqual(re_ordering('Mano donowana'), 'Mano donowana')

    def test_equal_3(self):
        self.assertEqual(re_ordering('wario LoBan hello'), 'LoBan wario hello')

    def test_equal_4(self):
        self.assertEqual(re_ordering('bull color pig Patrick'),
                         'Patrick bull color pig')

    def test_equal_5(self):
        self.assertEqual(re_ordering('jojo ddjajdiojdwo ana G nnibiial'),
                         'G jojo ddjajdiojdwo ana nnibiial')

    def test_equal_6(self):
        self.assertEqual(re_ordering(
            'is one of those rare names that s both exotic and simple Adira'
        ), 'Adira is one of those rare names that s both exotic and simple')

    def test_equal_7(self):
        self.assertEqual(re_ordering(
            'is an older name than annabel Amabel and a lot more distinctive'
        ), 'Amabel is an older name than annabel and a lot more distinctive')
