import unittest

from katas.kyu_7.new_5_pound_notes_collectors import get_new_notes


class GetNewNotesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(get_new_notes(2000, [500, 160, 400]), 188)

    def test_equal_2(self):
        self.assertEqual(get_new_notes(1260, [500, 50, 100]), 122)

    def test_equal_3(self):
        self.assertEqual(get_new_notes(3600, [1800, 350, 460, 500, 15]), 95)

    def test_equal_4(self):
        self.assertEqual(get_new_notes(1995, [1500, 19, 44]), 86)

    def test_equal_5(self):
        self.assertEqual(
            get_new_notes(10000, [1800, 500, 1200, 655, 150]), 1139)

    def test_equal_6(self):
        self.assertEqual(get_new_notes(2300, [590, 1500, 45, 655, 150]), 0)

    def test_equal_7(self):
        self.assertEqual(
            get_new_notes(5300, [1190, 1010, 1045, 55, 10, 19, 55]), 383)

    def test_equal_8(self):
        self.assertEqual(get_new_notes(2000, [500, 495, 100, 900]), 1)

    def test_equal_9(self):
        self.assertEqual(get_new_notes(2000, [500, 496, 100, 900]), 0)

    def test_equal_10(self):
        self.assertEqual(get_new_notes(2000, [500, 494, 100, 900]), 1)
