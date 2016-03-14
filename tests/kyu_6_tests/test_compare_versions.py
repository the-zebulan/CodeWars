import unittest

from katas.kyu_6.compare_versions import compare_versions


class CompareVersionsTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(compare_versions('11', '10'))

    def test_true_2(self):
        self.assertTrue(compare_versions('11', '11'))

    def test_true_3(self):
        self.assertTrue(compare_versions('10.4.6', '10.4'))

    def test_false(self):
        self.assertFalse(compare_versions('10.4', '10.4.8'))

    def test_false_2(self):
        self.assertFalse(compare_versions('10.4', '11'))

    def test_false_3(self):
        self.assertFalse(compare_versions('10.4', '10.10'))

    def test_false_4(self):
        self.assertFalse(compare_versions('10.4.9', '10.5'))


if __name__ == '__main__':
    unittest.main()
