import unittest

from katas.kyu_8.no_zeros_for_heros import no_boring_zeros


class NoBoringZerosTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(no_boring_zeros(1450), 145)

    def test_equals_2(self):
        self.assertEqual(no_boring_zeros(960000), 96)

    def test_equals_3(self):
        self.assertEqual(no_boring_zeros(1050), 105)

    def test_equals_4(self):
        self.assertEqual(no_boring_zeros(-1050), -105)

    def test_equals_5(self):
        self.assertEqual(no_boring_zeros(0), 0)
