import unittest

from katas.beta.file_path_operations import FileMaster


class FileMasterTestCase(unittest.TestCase):
    def setUp(self):
        self.fm = FileMaster('/Users/person1/Pictures/house.png')
        self.fm_2 = FileMaster('/Users/person1/Documents/addition.js')

    def test_equal_1(self):
        self.assertEqual(self.fm.extension(), 'png')

    def test_equal_2(self):
        self.assertEqual(self.fm.filename(), 'house')

    def test_equal_3(self):
        self.assertEqual(self.fm.dirpath(), '/Users/person1/Pictures/')

    def test_equal_4(self):
        self.assertEqual(self.fm_2.extension(), 'js')

    def test_equal_5(self):
        self.assertEqual(self.fm_2.filename(), 'addition')

    def test_equal_6(self):
        self.assertEqual(self.fm_2.dirpath(), '/Users/person1/Documents/')
