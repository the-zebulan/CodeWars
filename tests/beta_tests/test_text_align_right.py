import unittest

from katas.beta.text_align_right import align_right


class AlignRightTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(align_right('abc def', 10), '   abc def')

    def test_equal_2(self):
        self.assertEqual(align_right('I take up the whole line', 24),
                         'I take up the whole line')

    def test_equal_3(self):
        self.assertEqual(align_right('Two lines, I am', 10),
                         'Two lines,\n      I am')
