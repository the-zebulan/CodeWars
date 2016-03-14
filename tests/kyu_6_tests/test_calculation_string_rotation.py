import unittest

from kyu_6.calculate_string_rotation import shifted_diff


class ShiftedDiffTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(shifted_diff('coffee', 'eecoff'), 2)

    def test_equals_2(self):
        self.assertEqual(shifted_diff('eecoff', 'coffee'), 4)

    def test_equals_3(self):
        self.assertEqual(shifted_diff('moose', 'Moose'), -1)

    def test_equals_4(self):
        self.assertEqual(shifted_diff('isn\'t', '\'tisn'), 2)

    def test_equals_5(self):
        self.assertEqual(shifted_diff('Esham', 'Esham'), 0)

    def test_equals_6(self):
        self.assertEqual(shifted_diff('dog', 'god'), -1)

    def test_equals_7(self):
        self.assertEqual(shifted_diff('yoyo', 'oyoyoy'), -1)


if __name__ == '__main__':
    unittest.main()
