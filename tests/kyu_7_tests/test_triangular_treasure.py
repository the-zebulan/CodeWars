import unittest

from katas.kyu_7.triangular_treasure import triangular


class TriangularTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(triangular(0), 0)

    def test_equals_2(self):
        self.assertEqual(triangular(2), 3)

    def test_equals_3(self):
        self.assertEqual(triangular(3), 6)

    def test_equals_4(self):
        self.assertEqual(triangular(-10), 0)

    def test_equals_5(self):
        self.assertEqual(triangular(613827063227449),
                         188391831775217643091685137525)
