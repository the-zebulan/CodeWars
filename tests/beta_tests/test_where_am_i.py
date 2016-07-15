import unittest
from os import uname
from socket import gethostname

from katas.beta.where_am_i import get_pid


class WhereAmITestCase(unittest.TestCase):
    def setUp(self):
        self.pid = get_pid()

    def test_equal_1(self):
        self.assertEqual(self.pid, uname()[1])

    def test_equal_2(self):
        self.assertEqual(self.pid, gethostname())
