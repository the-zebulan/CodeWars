import re
import unittest

from Kyu_6.parse_the_log import logparser


class LogparserTestCase(unittest.TestCase):
    def setUp(self):
        self.regex = re.compile(logparser)

    def test_equals(self):
        self.assertEqual(self.regex.findall(
            '2003-07-08 16:49:45,896 ERROR [user1:mainfunction:subfunction] '
            'We have a problem'),
            [('2003-07-08 16:49:45,896', 'ERROR', 'user1', 'mainfunction',
              'subfunction', 'We have a problem')])

    def test_equals_2(self):
        self.assertEqual(self.regex.findall(
            '2003-07-08 16:49:46,896 INFO [user1:mainfunction] We don\'t hav'
            'e a problem'),
            [('2003-07-08 16:49:46,896', 'INFO', 'user1', 'mainfunction', '',
              'We don\'t have a problem')])

    def test_equals_3(self):
        self.assertEqual(len(self.regex.findall(
            '2003-07-08 16:49:45,896 ERROR [user1:mainfunction:subfunction] '
            'We have a problem')[0]), 6)


if __name__ == '__main__':
    unittest.main()
