import unittest

from katas.kyu_7.html_generator import HTMLGen


class HTMLGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.test = HTMLGen()

    def test_equals(self):
        self.assertEqual(self.test.a('test'), '<a>test</a>')

    def test_equals_2(self):
        self.assertEqual(self.test.comment('test'), '<!--test-->')

    def test_equals_3(self):
        self.assertEqual(self.test.title('hmm'), '<title>hmm</title>')
