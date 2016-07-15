import unittest

from katas.kyu_7.string_basics import get_users_ids


class GetUsersIDsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_users_ids('uid12345'), ['12345'])

    def test_equal_2(self):
        self.assertEqual(get_users_ids('   uidabc  '), ['abc'])

    def test_equal_3(self):
        self.assertEqual(get_users_ids('#uidswagger'), ['swagger'])

    def test_equal_4(self):
        self.assertEqual(get_users_ids('uidone, uidtwo'), ['one', 'two'])

    def test_equal_5(self):
        self.assertEqual(get_users_ids('uidCAPSLOCK'), ['capslock'])

    def test_equal_6(self):
        self.assertEqual(get_users_ids('uid##doublehashtag'),
                         ['doublehashtag'])

    def test_equal_7(self):
        self.assertEqual(get_users_ids('  uidin name whitespace'),
                         ['in name whitespace'])

    def test_equal_8(self):
        self.assertEqual(get_users_ids('uidMultipleuid'), ['multipleuid'])

    def test_equal_9(self):
        self.assertEqual(get_users_ids('uid12 ab, uid#, uidMiXeDcHaRs'),
                         ['12 ab', '', 'mixedchars'])

    def test_equal_10(self):
        self.assertEqual(get_users_ids(' uidT#e#S#t# '), ['test'])
