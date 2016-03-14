import unittest

from katas.beta.geometric_progression import geometric_sequence_elements


class GeometricSequenceElementsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(geometric_sequence_elements(2, 3, 5),
                         '2, 6, 18, 54, 162')

    def test_equals_2(self):
        self.assertEqual(geometric_sequence_elements(2, 2, 10),
                         '2, 4, 8, 16, 32, 64, 128, 256, 512, 1024')

    def test_equals_3(self):
        self.assertEqual(geometric_sequence_elements(1, -2, 10),
                         '1, -2, 4, -8, 16, -32, 64, -128, 256, -512')


if __name__ == '__main__':
    unittest.main()
