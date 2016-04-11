import unittest

from katas.kyu_8.add_more_item_to_list import AddExtra


class AddExtraTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(len(AddExtra([1, 2])), 3)

    def test_equals_2(self):
        self.assertEqual(len(AddExtra([])), 1)


if __name__ == '__main__':
    unittest.main()
