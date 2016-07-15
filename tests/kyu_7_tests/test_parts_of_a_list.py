import unittest

from katas.kyu_7.parts_of_a_list import partlist


class PartsListTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(partlist(["I", "wish", "I", "hadn't", "come"]), [
            ("I", "wish I hadn't come"), ("I wish", "I hadn't come"),
            ("I wish I", "hadn't come"), ("I wish I hadn't", "come")
        ])

    def test_equal_2(self):
        self.assertEqual(partlist(["cdIw", "tzIy", "xDu", "rThG"]), [
            ("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"),
            ("cdIw tzIy xDu", "rThG")
        ])

    def test_equal_3(self):
        self.assertEqual(partlist(["vJQ", "anj", "mQDq", "sOZ"]), [
            ("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"),
            ("vJQ anj mQDq", "sOZ")
        ])
