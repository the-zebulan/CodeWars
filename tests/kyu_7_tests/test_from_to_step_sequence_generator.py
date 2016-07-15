import unittest

from katas.kyu_7.from_to_step_sequence_generator import generator


class SequenceGeneratorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(generator(10, 20, 10), [10, 20])

    def test_equals_2(self):
        self.assertEqual(generator(10, 20, 1),
                         [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

    def test_equals_3(self):
        self.assertEqual(generator(10, 20, 5), [10, 15, 20])

    def test_equals_4(self):
        self.assertEqual(generator(10, 20, 7), [10, 17])

    def test_equals_5(self):
        self.assertEqual(generator(20, 10, 2), [20, 18, 16, 14, 12, 10])

    def test_equals_6(self):
        self.assertEqual(generator(20, 10, 0), [])

    def test_equals_7(self):
        self.assertEqual(generator(10, 20, -5), [])
