import unittest

from katas.kyu_7.hit_count import counter_effect


class CounterEffectTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(counter_effect('1250'),
                         [[0, 1], [0, 1, 2], [0, 1, 2, 3, 4, 5], [0]])

    def test_equal_2(self):
        self.assertEqual(counter_effect('0050'),
                         [[0], [0], [0, 1, 2, 3, 4, 5], [0]])

    def test_equal_3(self):
        self.assertEqual(counter_effect('0000'), [[0], [0], [0], [0]])
