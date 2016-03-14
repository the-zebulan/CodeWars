import unittest

from katas.kyu_6.remove_anchor_from_url import remove_url_anchor


class RemoveURLAnchorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(remove_url_anchor('www.codewars.com#about'),
                         'www.codewars.com')

    def test_equals_2(self):
        self.assertEqual(remove_url_anchor('www.codewars.com?page=1'),
                         'www.codewars.com?page=1')


if __name__ == '__main__':
    unittest.main()
