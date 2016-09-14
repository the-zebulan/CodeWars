import unittest

from katas.beta.separate_filename_from_extension import \
    separate_filename_from_extension


class SeparateFilenameFromExtensionTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(separate_filename_from_extension(
            '/some/path/to/file.txt'
        ), ('/some/path/to/file', '.txt'))

    def test_equal_2(self):
        self.assertEqual(separate_filename_from_extension(
            '/some/path/.to/.file.txt'
        ), ('/some/path/.to/.file', '.txt'))

    def test_equal_3(self):
        self.assertEqual(separate_filename_from_extension(
            '/some/path/.to/.file.tar.gz'
        ), ('/some/path/.to/.file', '.tar.gz'))
