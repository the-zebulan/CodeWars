import unittest
from textwrap import dedent

from katas.kyu_7.thinkful_string_drills_poem_formatter import format_poem


class FormatPoemTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(format_poem(
            'Beautiful is better than ugly. '
            'Explicit is better than implicit. '
            'Simple is better than complex. '
            'Complex is better than complicated.'),
            dedent('''\
                Beautiful is better than ugly.
                Explicit is better than implicit.
                Simple is better than complex.
                Complex is better than complicated.'''))

    def test_equal_2(self):
        self.assertEqual(format_poem(
            "Flat is better than nested. "
            "Sparse is better than dense. "
            "Readability counts. "
            "Special cases aren't special enough to break the rules."),
            dedent('''\
                Flat is better than nested.
                Sparse is better than dense.
                Readability counts.
                Special cases aren't special enough to break the rules.'''))

    def test_equal_3(self):
        self.assertEqual(format_poem(
            "Although practicality beats purity. "
            "Errors should never pass silently. "
            "Unless explicitly silenced. "
            "In the face of ambiguity, refuse the temptation to guess."),
            dedent('''\
                Although practicality beats purity.
                Errors should never pass silently.
                Unless explicitly silenced.
                In the face of ambiguity, refuse the temptation to guess.'''))
