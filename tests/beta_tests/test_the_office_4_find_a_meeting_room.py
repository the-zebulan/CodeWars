import unittest

from katas.beta.the_office_4_find_a_meeting_room import meeting


class MeetingTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(meeting(['X', 'O', 'X']), 1)

    def test_equal_2(self):
        self.assertEqual(meeting(['O', 'X', 'X', 'X', 'X']), 0)

    def test_equal_3(self):
        self.assertEqual(meeting(['X', 'X', 'O', 'X', 'X']), 2)

    def test_equal_4(self):
        self.assertEqual(meeting(['X']), 'None available!')
