import unittest

from katas.kyu_7.bug_fixing_unfinished_loop import create_array


class CreateArrayTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(create_array(1), [1])

    def test_equals_2(self):
        self.assertEqual(create_array(2), [1, 2])

    def test_equals_3(self):
        self.assertEqual(create_array(3), [1, 2, 3])

    def test_equals_4(self):
        self.assertEqual(create_array(4), [1, 2, 3, 4])

    def test_equals_5(self):
        self.assertEqual(create_array(5), [1, 2, 3, 4, 5])
