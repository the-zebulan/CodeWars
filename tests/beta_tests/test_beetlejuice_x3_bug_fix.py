import unittest

from katas.beta.beetlejuice_x3_bug_fix import beetle_juice


class BeetleJuiceTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(beetle_juice("Harry!"), "Harry!  Harry!  Harry!")

    def test_equal_2(self):
        self.assertEqual(beetle_juice("Hobie!"), "Hobie!  Hobie!  Hobie!")

    def test_equal_3(self):
        self.assertEqual(beetle_juice("Sheila!"), "Sheila!  Sheila!  Sheila!")

    def test_equal_4(self):
        self.assertEqual(beetle_juice("Shoshanna!"),
                         "Shoshanna!  Shoshanna!  Shoshanna!")
