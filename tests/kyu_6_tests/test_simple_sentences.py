import unittest

from katas.kyu_6.simple_sentences import make_sentences


class MakeSentencesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(make_sentences(['hello', 'world']), 'hello world.')

    def test_equals_2(self):
        self.assertEqual(make_sentences(
            ['Quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']),
            'Quick brown fox jumped over the lazy dog.')

    def test_equals_3(self):
        self.assertEqual(make_sentences(['hello', ',', 'my', 'dear']),
                         'hello, my dear.')

    def test_equals_4(self):
        self.assertEqual(make_sentences(['one', ',', 'two', ',', 'three']),
                         'one, two, three.')

    def test_equals_5(self):
        self.assertEqual(make_sentences(
            ['One', ',', 'two', 'two', ',', 'three', 'three', 'three', ',',
             '4', '4', '4', '4']), 'One, two two, three three three, 4 4 4 4.')

    def test_equals_6(self):
        self.assertEqual(make_sentences(['hello', 'world', '.']),
                         'hello world.')

    def test_equals_7(self):
        self.assertEqual(make_sentences(['Bye', '.']), 'Bye.')

    def test_equals_8(self):
        self.assertEqual(make_sentences(['hello', 'world', '.', '.', '.']),
                         'hello world.')

    def test_equals_9(self):
        self.assertEqual(make_sentences(
            ['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365',
             'days', ',', 'I', 'know', 'that', '.', '.', '.', '.', '.', '.',
             '.', '.', '.', '.', '.', '.']),
            'The Earth rotates around The Sun in 365 days, I know that.')
