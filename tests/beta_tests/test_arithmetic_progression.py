import unittest

from beta.arithmetic_progression import arithmetic_sequence_elements


class ArithmeticSequenceTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(
            arithmetic_sequence_elements(1, 2, 5), '1, 3, 5, 7, 9')

    def test_equals_2(self):
        self.assertEqual(arithmetic_sequence_elements(1, -3, 10),
                         '1, -2, -5, -8, -11, -14, -17, -20, -23, -26')


if __name__ == '__main__':
    unittest.main()
