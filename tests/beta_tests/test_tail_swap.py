import unittest

from katas.beta.tail_swap import tail_swap


class TailSwapTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(tail_swap(['abc:123', 'cde:456']),
                         ['abc:456', 'cde:123'])

    def test_equal_2(self):
        self.assertEqual(tail_swap(['a:12345', '777:xyz']),
                         ['a:xyz', '777:12345'])
