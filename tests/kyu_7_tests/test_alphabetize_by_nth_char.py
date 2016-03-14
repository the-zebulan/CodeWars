import unittest

from kyu_7.alphabetize_by_nth_char import sort_it


class SortItTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(sort_it('bid, zag', 2), 'zag, bid')

    def test_equals_2(self):
        self.assertEqual(sort_it('bill, bell, ball, bull', 2),
                         'ball, bell, bill, bull')

    def test_equals_3(self):
        self.assertEqual(sort_it('cat, dog, eel, bee', 3),
                         'bee, dog, eel, cat')


if __name__ == '__main__':
    unittest.main()
