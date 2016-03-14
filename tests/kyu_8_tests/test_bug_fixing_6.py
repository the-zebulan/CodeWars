import unittest

from kyu_8.bug_fixing_6 import eval_object


class EvalObjectTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(eval_object({'a': 1, 'b': 1, 'operation': '+'}), 2)

    def test_equals_2(self):
        self.assertEqual(eval_object({'a': 1, 'b': 1, 'operation': '-'}), 0)

    def test_equals_3(self):
        self.assertEqual(eval_object({'a': 1, 'b': 1, 'operation': '/'}), 1)

    def test_equals_4(self):
        self.assertEqual(eval_object({'a': 1, 'b': 1, 'operation': '*'}), 1)

    def test_equals_5(self):
        self.assertEqual(eval_object({'a': 1, 'b': 1, 'operation': '%'}), 0)

    def test_equals_6(self):
        self.assertEqual(eval_object({'a': 1, 'b': 1, 'operation': '**'}), 1)


if __name__ == '__main__':
    unittest.main()
