import unittest

from katas.beta.split_string_by_multiple_delimiters import multiple_split


class MultipleSplitTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(multiple_split('Hi, how are you?', [' ']),
                         ['Hi,', 'how', 'are', 'you?'])

    def test_equal_2(self):
        self.assertEqual(multiple_split('Hi, how are you?', []),
                         ['Hi, how are you?'])

    def test_equal_3(self):
        self.assertEqual(multiple_split('1+2-3', ['+', '-']),
                         ['1', '2', '3'])

    def test_equal_4(self):
        self.assertEqual(multiple_split('Hi everybody!', [' ', '!']),
                         ['Hi', 'everybody'])

    def test_equal_5(self):
        self.assertEqual(multiple_split(
            '(1+2)*6-3^9', ['+', '-', '(', ')', '^', '*']
        ), ['1', '2', '6', '3', '9'])

    def test_equal_6(self):
        self.assertEqual(multiple_split(
            'Solve_this|kata-very\quickly!', ['!', '|', '\\', '_', '-']
        ), ['Solve', 'this', 'kata', 'very', 'quickly'])

    def test_equal_7(self):
        self.assertEqual(multiple_split(
            '(1+2)*6-3^9', ['+', '-', '(', ')', '^', '*']
        ), ['1', '2', '6', '3', '9'])

    def test_equal_8(self):
        self.assertEqual(multiple_split('some strange string'),
                         ['some strange string'])

    def test_equal_9(self):
        self.assertEqual(multiple_split('', []), [])

    def test_equal_10(self):
        self.assertEqual(multiple_split(''), [])

    def test_equal_11(self):
        self.assertEqual(multiple_split('1_2_3_huhuh_hahaha', ['_']),
                         ['1', '2', '3', 'huhuh', 'hahaha'])

    def test_equal_12(self):
        self.assertEqual(multiple_split(
            '((1+2))*(6-3)^9', ['+', '-', '(', ')', '^', '*']
        ), ['1', '2', '6', '3', '9'])

    def test_equal_13(self):
        self.assertEqual(multiple_split('(((1+2)-(3)))', ['(', ')']),
                         ['1+2', '-', '3'])
