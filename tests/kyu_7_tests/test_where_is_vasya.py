import unittest

from kyu_7.where_is_vasya import where_is_he


class WhereIsHeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(where_is_he(3, 1, 1), 2)

    def test_equals_2(self):
        self.assertEqual(where_is_he(5, 2, 3), 3)

    def test_equals_3(self):
        self.assertEqual(where_is_he(6, 5, 5), 1)

    def test_equals_4(self):
        self.assertEqual(where_is_he(5, 4, 0), 1)

    def test_equals_5(self):
        self.assertEqual(where_is_he(9, 4, 3), 4)


if __name__ == '__main__':
    unittest.main()
