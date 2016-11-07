import unittest

from katas.beta.identify_case import case_id


class CaseIdTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(case_id('hello-world'), 'kebab')

    def test_equal_2(self):
        self.assertEqual(case_id('hello-to-the-world'), 'kebab')

    def test_equal_3(self):
        self.assertEqual(case_id('helloWorld'), 'camel')

    def test_equal_4(self):
        self.assertEqual(case_id('helloToTheWorld'), 'camel')

    def test_equal_5(self):
        self.assertEqual(case_id('hello_world'), 'snake')

    def test_equal_6(self):
        self.assertEqual(case_id('hello_to_the_world'), 'snake')

    def test_equal_7(self):
        self.assertEqual(case_id('hello__world'), 'none')

    def test_equal_8(self):
        self.assertEqual(case_id('hello_World'), 'none')

    def test_equal_9(self):
        self.assertEqual(case_id('helloworld'), 'none')

    def test_equal_10(self):
        self.assertEqual(case_id('hello-World'), 'none')

    def test_equal_11(self):
        self.assertEqual(case_id('hello-World'), 'none')

    def test_equal_12(self):
        self.assertEqual(case_id('hello-To-The-World'), 'none')

    def test_equal_13(self):
        self.assertEqual(case_id('good-Night'), 'none')

    def test_equal_14(self):
        self.assertEqual(case_id('he--llo'), 'none')
