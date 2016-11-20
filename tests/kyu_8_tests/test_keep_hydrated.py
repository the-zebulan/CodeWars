import unittest

from katas.kyu_8.keep_hydrated import litres


class LitresTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(litres(2), 1)

    def test_equal_2(self):
        self.assertEqual(litres(1.4), 0)

    def test_equal_3(self):
        self.assertEqual(litres(12.3), 6)

    def test_equal_4(self):
        self.assertEqual(litres(0.82), 0)

    def test_equal_5(self):
        self.assertEqual(litres(11.8), 5)

    def test_equal_6(self):
        self.assertEqual(litres(1787), 893)

    def test_equal_7(self):
        self.assertEqual(litres(0), 0)
