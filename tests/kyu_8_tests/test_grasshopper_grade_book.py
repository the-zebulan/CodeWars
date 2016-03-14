import unittest

from kyu_8.grasshopper_grade_book import get_grade


class GetGradeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(get_grade(95, 90, 93), 'A')

    def test_equals_2(self):
        self.assertEqual(get_grade(100, 85, 96), 'A')

    def test_equals_3(self):
        self.assertEqual(get_grade(92, 93, 94), 'A')

    def test_equals_4(self):
        self.assertEqual(get_grade(70, 70, 100), 'B')

    def test_equals_5(self):
        self.assertEqual(get_grade(82, 85, 87), 'B')

    def test_equals_6(self):
        self.assertEqual(get_grade(84, 79, 85), 'B')

    def test_equals_7(self):
        self.assertEqual(get_grade(70, 70, 70), 'C')

    def test_equals_8(self):
        self.assertEqual(get_grade(75, 70, 79), 'C')

    def test_equals_9(self):
        self.assertEqual(get_grade(60, 82, 76), 'C')

    def test_equals_10(self):
        self.assertEqual(get_grade(65, 70, 59), 'D')

    def test_equals_11(self):
        self.assertEqual(get_grade(66, 62, 68), 'D')

    def test_equals_12(self):
        self.assertEqual(get_grade(58, 62, 70), 'D')

    def test_equals_13(self):
        self.assertEqual(get_grade(44, 55, 52), 'F')

    def test_equals_14(self):
        self.assertEqual(get_grade(48, 55, 52), 'F')

    def test_equals_15(self):
        self.assertEqual(get_grade(58, 59, 60), 'F')


if __name__ == '__main__':
    unittest.main()
