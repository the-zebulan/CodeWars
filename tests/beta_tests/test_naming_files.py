import unittest

from katas.beta.naming_files import name_file


class NameFileTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(name_file('IMG <index_no>', 4, 1),
                         ['IMG 1', 'IMG 2', 'IMG 3', 'IMG 4'])

    def test_equal_2(self):
        self.assertEqual(name_file('image #<index_no>.jpg', 3, 7),
                         ['image #7.jpg', 'image #8.jpg', 'image #9.jpg'])

    def test_equal_3(self):
        self.assertEqual(name_file('#<index_no> #<index_no>', 3, -2),
                         ['#-2 #-2', '#-1 #-1', '#0 #0'])

    def test_equal_4(self):
        self.assertEqual(name_file('<file> number <index_no>', 5, 0), [
            '<file> number 0', '<file> number 1', '<file> number 2',
            '<file> number 3', '<file> number 4'])

    def test_equal_5(self):
        self.assertEqual(name_file('<file_no> number <index_no>', 2, -1),
                         ['<file_no> number -1', '<file_no> number 0'])

    def test_equal_6(self):
        self.assertEqual(name_file('file', 2, 3), ['file', 'file'])

    def test_equal_7(self):
        self.assertEqual(name_file('<file_no> number <index_no>', -1, 0), [])

    def test_equal_8(self):
        self.assertEqual(name_file('file <index_no>', 2, 0.1), [])

    def test_equal_9(self):
        self.assertEqual(name_file('file <index_no>', 0.2, 0), [])

    def test_equal_10(self):
        self.assertEqual(name_file('file <index_no>', 0, 0), [])
