import unittest

from katas.beta.the_skeptical_kid_generator import alan_annoying_kid


class AlanAnnoyingKidTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(alan_annoying_kid("Today I played football."),
                         "I don't think you played football today, I think y"
                         "ou didn't play at all!")

    def test_equal_2(self):
        self.assertEqual(alan_annoying_kid("Today I didn't play football."),
                         "I don't think you didn't play football today, I th"
                         "ink you did play it!")

    def test_equal_3(self):
        self.assertEqual(alan_annoying_kid(
            "Today I didn't attempt to hardcode this Kata."
        ), "I don't think you didn't attempt to hardcode this Kata today, I"
           " think you did attempt it!")

    def test_equal_4(self):
        self.assertEqual(alan_annoying_kid("Today I cleaned the kitchen."),
                         "I don't think you cleaned the kitchen today, I thi"
                         "nk you didn't clean at all!")

    def test_equal_5(self):
        self.assertEqual(alan_annoying_kid(
            "Today I learned to code like a pro."
        ), "I don't think you learned to code like a pro today, I think you "
           "didn't learn at all!")


if __name__ == '__main__':
    unittest.main()
