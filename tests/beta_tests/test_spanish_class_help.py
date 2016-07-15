import unittest

from katas.beta.spanish_class_help import gender


class SpanishClassHelpTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(gender('genio'), ['el genio'])

    def test_equals_2(self):
        self.assertEqual(gender('chico', 'esquinas'),
                         ['el chico', 'las esquinas'])

    def test_equals_3(self):
        self.assertEqual(gender('parques'), ['los parques'])

    def test_equals_4(self):
        self.assertEqual(gender('vino', 5, None), ['el vino', 5, None])

    def test_equals_5(self):
        self.assertEqual(gender('lampas'), ['las lampas'])
