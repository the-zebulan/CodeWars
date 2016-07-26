import unittest

from katas.kyu_8.pole_vault_starting_marks import starting_mark


class StartingMarkTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(starting_mark(1.52), 9.45)

    def test_equal_2(self):
        self.assertEqual(starting_mark(1.83), 10.67)

    def test_equal_3(self):
        self.assertEqual(starting_mark(1.22), 8.27)

    def test_equal_4(self):
        self.assertEqual(starting_mark(2.13), 11.85)

    def test_equal_5(self):
        self.assertEqual(starting_mark(1.75), 10.36)
