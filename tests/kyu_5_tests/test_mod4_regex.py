import re
import unittest

from katas.kyu_5.mod4_regex import Mod


class Mod4RegexTestCase(unittest.TestCase):
    """ assertRegexpMatches doesn't seem to work properly for the tests
    since Mod.mod4 is a compiled regex object already, not just a string.
    To match the tests used on the Codewars kata, I used assertIsNone
    and assertIsNotNone for the tests instead. """

    def setUp(self):
        self.invalid_tests = iter([
            '[+05621]', '[-55622]', '[005623]', '[~24]', '[8.04]',
            "No, [2014] isn't a multiple of 4..."]
        )
        self.valid_tests = iter([
            '[+05620]', '[005624]', '[-05628]', '[005632]', '[555636]',
            '[+05640]', '[005600]', 'the beginning [-0] the end', '~[4]',
            '[32]', 'the beginning [0] ... [invalid] numb[3]rs ... the end',
            '...may be [+002016] will be.'
        ])

    def test_is_instance_1(self):
        """ According to this stackoverflow, the proper way to check that
        Mod.mod4 is a regex object is debatable. Here are two ways.
        https://stackoverflow.com/questions/6226180/detect-re-regexp-object-in-python
        """
        self.assertIsInstance(Mod.mod4, re._pattern_type)
        # self.assertEqual(type(Mod.mod4), type(re.compile('')))

    def test_is_none_1(self):
        self.assertIsNone(Mod.mod4.match(next(self.invalid_tests)))

    def test_is_none_2(self):
        self.assertIsNone(Mod.mod4.match(next(self.invalid_tests)))

    def test_is_none_3(self):
        self.assertIsNone(Mod.mod4.match(next(self.invalid_tests)))

    def test_is_none_4(self):
        self.assertIsNone(Mod.mod4.match(next(self.invalid_tests)))

    def test_is_none_5(self):
        self.assertIsNone(Mod.mod4.match(next(self.invalid_tests)))

    def test_is_none_6(self):
        self.assertIsNone(Mod.mod4.match(next(self.invalid_tests)))

    def test_is_not_none_1(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_2(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_3(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_4(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_5(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_6(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_7(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_8(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_9(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_10(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_11(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))

    def test_is_not_none_12(self):
        self.assertIsNotNone(Mod.mod4.match(next(self.valid_tests)))
