import unittest

from katas.kyu_5.prefill_an_array import prefill


class PrefillTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(prefill(3, 1), [1, 1, 1])

    def test_equals_2(self):
        self.assertEqual(prefill(2, 'abc'), ['abc', 'abc'])

    def test_equals_3(self):
        self.assertEqual(prefill('1', 1), [1])

    def test_equals_4(self):
        self.assertEqual(prefill(3, prefill(2, '2d')),
                         [['2d', '2d'], ['2d', '2d'], ['2d', '2d']])

    def test_raises_1(self):
        self.assertRaises(TypeError, prefill, 'z', 3)

    def test_raises_2(self):
        self.assertRaises(TypeError, prefill, lambda: 1, 5)
