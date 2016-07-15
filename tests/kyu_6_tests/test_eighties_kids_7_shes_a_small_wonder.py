import unittest

from katas.kyu_6.eighties_kids_7_shes_a_small_wonder import Robot


class RobotTestCase(unittest.TestCase):
    def setUp(self):
        self.vicky = Robot()

    def test_equals(self):
        self.assertEqual(self.vicky.learn_word('hello'),
                         'Thank you for teaching me hello')

    def test_equals_2(self):
        self.assertEqual(self.vicky.learn_word('world'),
                         'Thank you for teaching me world')
        self.assertEqual(self.vicky.learn_word('World'),
                         'I already know the word World')
        self.assertEqual(self.vicky.learn_word('world'),
                         'I already know the word world')

    def test_equals_3(self):
        self.assertEqual(self.vicky.learn_word('goodbye'),
                         'Thank you for teaching me goodbye')

    def test_equals_4(self):
        self.assertEqual(self.vicky.learn_word('Thank'),
                         'I already know the word Thank')
