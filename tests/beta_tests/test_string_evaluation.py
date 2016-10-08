import unittest

from katas.beta.string_evaluation import string_evaluation


class StringEvaluationTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(string_evaluation(
            'aab#HcCcc##l#', ['a<b', '#==4', 'c>=C', 'H!=a']
        ), [False, True, True, True])

    def test_equal_2(self):
        self.assertEqual(string_evaluation(
            'abc#$%KDAyyaa@@@', ['#>@', 'A==2', 'a>A', '$!=2']
        ), [False, False, True, True])

    def test_equal_3(self):
        self.assertEqual(string_evaluation(
            'abb', ['a>b', 'b==a', 'b<=a', 'b>a', 'b!=b', 'a==1', 'b==1']
        ), [False, False, False, True, False, True, False])
