import unittest

from katas.kyu_7.make_backronym import make_backronym


class MakeBackronymTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(make_backronym('interesting'),
                         'ingestable newtonian turn eager rant eager stylish'
                         ' turn ingestable newtonian gregarious')

    def test_equals_2(self):
        self.assertEqual(make_backronym('codewars'),
                         'confident oscillating disturbing eager weird aweso'
                         'me rant stylish')


if __name__ == '__main__':
    unittest.main()
