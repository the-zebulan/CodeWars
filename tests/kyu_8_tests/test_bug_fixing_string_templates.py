import unittest

from katas.kyu_8.bug_fixing_string_templates import build_string


class BuildStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(build_string('Cheese', 'Milk', 'Chocolate'),
                         'I like Cheese, Milk, Chocolate!')

    def test_equals_2(self):
        self.assertEqual(build_string('Cheese', 'Milk'),
                         'I like Cheese, Milk!')

    def test_equals_3(self):
        self.assertEqual(build_string('Chocolate'), 'I like Chocolate!')


if __name__ == '__main__':
    unittest.main()
