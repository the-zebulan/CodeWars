import unittest

from katas.kyu_7.html_generator import HTMLGen


class HTMLGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.html = HTMLGen()

    def test_equal_1(self):
        self.assertEqual(self.html.a('test'), '<a>test</a>')

    def test_equal_2(self):
        self.assertEqual(self.html.comment('test'), '<!--test-->')

    def test_equal_3(self):
        self.assertEqual(self.html.title('test'), '<title>test</title>')

    def test_equal_4(self):
        self.assertEqual(self.html.b('test'), '<b>test</b>')

    def test_equal_5(self):
        self.assertEqual(self.html.p('test'), '<p>test</p>')

    def test_equal_6(self):
        self.assertEqual(self.html.body('test'), '<body>test</body>')

    def test_equal_7(self):
        self.assertEqual(self.html.div('test'), '<div>test</div>')

    def test_equal_8(self):
        self.assertEqual(self.html.span('test'), '<span>test</span>')
