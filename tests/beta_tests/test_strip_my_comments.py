import unittest

from katas.beta.strip_my_comments import strip_it


class StripMyCommentsTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(strip_it('var Foo = 1;// Foo declared'), 'var Foo = 1;')

    def test_equals_2(self):
        self.assertEqual(strip_it('1 + /* 2 */3'), '1 + 3')

    def test_equals_3(self):
        self.assertEqual(strip_it('1 /* a */+/* b */ 1'), '1 + 1')

    def test_equals_4(self):
        self.assertEqual(strip_it(' x = 10;// ten !'), ' x = 10;')
