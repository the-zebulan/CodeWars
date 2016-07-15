import unittest

from katas.kyu_3.finding_an_appointment import get_start_time


class GetStartTimeTestCase(unittest.TestCase):
    def setUp(self):
        self.schedule_1 = [
            [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'],
             ['17:45', '19:00']],
            [['09:15', '12:00'], ['14:00', '16:30'], ['17:00', '17:30']],
            [['11:30', '12:15'], ['15:00', '16:30'], ['17:45', '19:00']]
        ]
        self.schedule_2 = [
            [['10:07', '10:39'], ['10:41', '11:03'], ['12:21', '12:22'],
             ['15:49', '16:11'], ['17:29', '17:54']],
            [['09:37', '11:19'], ['11:27', '13:37'], ['16:29', '17:41']],
            [['09:48', '12:26'], ['15:41', '15:59'], ['18:50', '18:57']],
            [['09:41', '09:57'], ['10:03', '10:14'], ['10:32', '10:39'],
             ['10:56', '11:17'], ['11:23', '11:41'], ['11:59', '12:03'],
             ['12:28', '12:45'], ['17:19', '17:27'], ['18:56', '18:57']],
            [['11:21', '12:42'], ['12:51', '13:20'], ['17:51', '17:53'],
             ['18:07', '18:11']]
        ]
        self.schedule_3 = [
            [['09:09', '11:27'], ['12:14', '13:41'], ['15:16', '17:17'],
             ['17:32', '18:50']],
            [['10:38', '12:06'], ['13:39', '15:08'], ['17:23', '17:26'],
             ['18:02', '18:26']]
        ]

    def test_equal_1(self):
        self.assertEqual(get_start_time(self.schedule_1, 60), '12:15')

    def test_equal_2(self):
        self.assertEqual(get_start_time(self.schedule_1, 75), '12:15')

    def test_equal_3(self):
        self.assertEqual(get_start_time([
            [['10:00', '13:00'], ['14:00', '17:00'], ['18:00', '19:00']],
            [['10:00', '11:00'], ['12:00', '13:00'], ['14:00', '15:00'],
             ['16:00', '17:00'], ['18:00', '19:00']]
        ], 60), '09:00')

    def test_equal_4(self):
        self.assertEqual(get_start_time(self.schedule_2, 37), '09:00')

    def test_equal_5(self):
        self.assertEqual(get_start_time(self.schedule_2, 38), '13:37')

    def test_equal_6(self):
        self.assertEqual(get_start_time(self.schedule_2, 124), '13:37')

    def test_equal_7(self):
        self.assertEqual(get_start_time(self.schedule_3, 9), '09:00')

    def test_equal_8(self):
        self.assertEqual(get_start_time(self.schedule_3, 10), '18:50')

    def test_is_none_1(self):
        self.assertIsNone(get_start_time(self.schedule_1, 76))

    def test_is_none_2(self):
        self.assertIsNone(get_start_time(self.schedule_1, 90))

    def test_is_none_3(self):
        self.assertIsNone(get_start_time(
            [[['09:00', '19:00']], [], [], []], 1
        ))

    def test_is_none_4(self):
        self.assertIsNone(get_start_time(self.schedule_2, 125))

    def test_is_none_5(self):
        self.assertIsNone(get_start_time(self.schedule_3, 11))
