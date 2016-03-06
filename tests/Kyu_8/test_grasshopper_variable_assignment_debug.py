import unittest

from Kyu_8.grasshopper_variable_assignment_debug import a, b, name


class VariablesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(a, 'dev')

    def test_equals_2(self):
        self.assertEqual(b, 'Lab')

    def test_equals_3(self):
        self.assertEqual(name, 'devLab')


if __name__ == '__main__':
    unittest.main()
