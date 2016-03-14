import unittest

from kyu_7.bug_fixing_class_conundrum import List


class ListTestCase(unittest.TestCase):
    def setUp(self):
        self.my_list = List(str)

    def test_equals(self):
        self.assertEqual(self.my_list.add('Hello').count, 1)
        self.assertEqual(self.my_list.add(' ').add('World!').count, 3)

    def test_equals_2(self):
        self.assertEqual(self.my_list.add(5),
                         'This item is not of type: str')


if __name__ == '__main__':
    unittest.main()
