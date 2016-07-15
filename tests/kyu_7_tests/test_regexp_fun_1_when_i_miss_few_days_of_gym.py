import unittest

from katas.kyu_7.regexp_fun_1_when_i_miss_few_days_of_gym import gym_slang


class GymSlangTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(gym_slang("When I miss few days of gym"),
                         "When I miss few days of gym")

    def test_equal_2(self):
        self.assertEqual(gym_slang("Squad probably think I am fake"),
                         "Squad prolly think I'm fake")

    def test_equal_3(self):
        self.assertEqual(
            gym_slang("Whole squad probably bigger than me now"),
            "Whole squad prolly bigger than me now"
        )

    def test_equal_4(self):
        self.assertEqual(
            gym_slang("No selfie to post on Instagram either"),
            "No selfie to post on Insta either"
        )

    def test_equal_5(self):
        self.assertEqual(
            gym_slang("Gym crush probably found someone else"),
            "Gym crush prolly found someone else"
        )

    def test_equal_6(self):
        self.assertEqual(gym_slang("What if I die fat"),
                         "What if I die fat")

    def test_equal_7(self):
        self.assertEqual(
            gym_slang("What if I do not fit in my clothes now"),
            "What if I don't fit in my clothes now"
        )

    def test_equal_8(self):
        self.assertEqual(
            gym_slang("Going to feel like a new gym member"),
            "Gonna feel like a new gym member"
        )

    def test_equal_9(self):
        self.assertEqual(
            gym_slang("wait what was my lock combination"),
            "wait what was my lock combo"
        )

    def test_equal_10(self):
        self.assertEqual(
            gym_slang("that skinny hoe can probably outlift me now"),
            "that skinny hoe can prolly outlift me now")

    def test_equal_11(self):
        self.assertEqual(gym_slang("probably Probably"), "prolly Prolly")

    def test_equal_12(self):
        self.assertEqual(gym_slang("i am I am"), "i'm I'm")

    def test_equal_13(self):
        self.assertEqual(gym_slang("instagram Instagram"), "insta Insta")

    def test_equal_14(self):
        self.assertEqual(gym_slang("do not Do not"), "don't Don't")

    def test_equal_15(self):
        self.assertEqual(gym_slang("going to Going to"), "gonna Gonna")

    def test_equal_16(self):
        self.assertEqual(gym_slang("combination Combination"), "combo Combo")

    def test_equal_17(self):
        self.assertEqual(
            gym_slang("probably Probably probably Probably probably Probabl"
                      "y probably Probably probably Probably"),
            "prolly Prolly prolly Prolly prolly Prolly prolly Prolly prolly"
            " Prolly"
        )

    def test_equal_18(self):
        self.assertEqual(gym_slang(
            "i am I am i am I am i am I am i am I am i am I am i am I am"
        ), "i'm I'm i'm I'm i'm I'm i'm I'm i'm I'm i'm I'm")

    def test_equal_19(self):
        self.assertEqual(gym_slang(
            "instagram Instagram instagram Instagram instagram Instagram in"
            "stagram Instagram instagram Instagram"
        ), "insta Insta insta Insta insta Insta insta Insta insta Insta")

    def test_equal_20(self):
        self.assertEqual(gym_slang(
            "do not Do not do not Do not do not Do not do not Do not"
        ), "don't Don't don't Don't don't Don't don't Don't")

    def test_equal_21(self):
        self.assertEqual(gym_slang(
            "Going to going to Going to Going to going to Going to Going to"
            " going to Going to"
        ), "Gonna gonna Gonna Gonna gonna Gonna Gonna gonna Gonna")

    def test_equal_22(self):
        self.assertEqual(gym_slang(
            "combination combination Combination combination Combination"
        ), "combo combo Combo combo Combo")
