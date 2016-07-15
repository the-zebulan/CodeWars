import unittest

from katas.kyu_5.pete_the_baker import cakes


class CakesTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(cakes(
            {'flour': 500, 'eggs': 1, 'sugar': 200},
            {'flour': 1200, 'eggs': 5, 'milk': 200, 'sugar': 1200}
        ), 2)

    def test_equal_2(self):
        self.assertEqual(cakes(
            {'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100,
             'cream': 200},
            {'flour': 20000, 'oil': 30000, 'cream': 5000, 'milk': 20000,
             'sugar': 1700}
        ), 11)

    def test_equal_3(self):
        self.assertEqual(cakes(
            {'flour': 300, 'oil': 100, 'milk': 100, 'apples': 3,
             'sugar': 150},
            {'flour': 2000, 'milk': 2000, 'sugar': 500}
        ), 0)

    def test_equal_4(self):
        self.assertEqual(cakes(
            {'flour': 300, 'oil': 100, 'milk': 100, 'apples': 3,
             'sugar': 150},
            {'flour': 2000, 'oil': 20, 'milk': 2000, 'apples': 15,
             'sugar': 500}
        ), 0)

    def test_equal_5(self):
        self.assertEqual(cakes(
            {'oil': 1, 'flour': 3, 'eggs': 1, 'sugar': 1, 'milk': 1,
             'cream': 1},
            {'oil': 1, 'flour': 3, 'eggs': 1, 'sugar': 1, 'milk': 1,
             'cream': 1}
        ), 1)

    def test_equal_6(self):
        self.assertEqual(cakes(
            {'flour': 37, 'apples': 1, 'chocolate': 66},
            {'butter': 8355, 'crumbles': 1884, 'flour': 2831, 'eggs': 1103,
             'nuts': 6781, 'pears': 9968, 'chocolate': 648, 'cocoa': 3517,
             'oil': 6860, 'apples': 9295, 'sugar': 9661, 'milk': 6523,
             'cream': 8340}
        ), 9)

    def test_equal_7(self):
        self.assertEqual(cakes(
            {'eggs': 92, 'nuts': 32, 'apples': 36},
            {'butter': 4143, 'crumbles': 485, 'flour': 5897, 'eggs': 4374,
             'nuts': 699, 'pears': 9208, 'sugar': 8574, 'cocoa': 4438,
             'oil': 7165, 'apples': 294, 'chocolate': 2601, 'milk': 5803,
             'cream': 5956}
        ), 8)

    def test_equal_8(self):
        self.assertEqual(cakes(
            {'crumbles': 94, 'milk': 100, 'chocolate': 96},
            {'butter': 4518, 'oil': 8691, 'flour': 4273, 'eggs': 5507,
             'nuts': 722, 'pears': 9097, 'chocolate': 6130, 'cocoa': 9660,
             'crumbles': 2880, 'apples': 3877, 'sugar': 821, 'milk': 8224,
             'cream': 5574}
        ), 30)

    def test_equal_9(self):
        self.assertEqual(cakes(
            {'eggs': 79, 'crumbles': 74, 'cream': 50},
            {'butter': 336, 'crumbles': 9186, 'flour': 9180, 'eggs': 8606,
             'nuts': 8204, 'pears': 2536, 'chocolate': 4520, 'cocoa': 1028,
             'oil': 1750, 'apples': 1638, 'sugar': 8427, 'milk': 1759,
             'cream': 6807}
        ), 108)

    def test_equal_10(self):
        self.assertEqual(cakes(
            {'butter': 36, 'eggs': 84, 'nuts': 53},
            {'butter': 2584, 'crumbles': 4229, 'flour': 5740, 'eggs': 4914,
             'nuts': 6756, 'pears': 7824, 'chocolate': 574, 'cocoa': 874,
             'oil': 3455, 'apples': 783, 'sugar': 7769, 'milk': 817,
             'cream': 5206}
        ), 58)

    def test_equal_11(self):
        self.assertEqual(cakes({'flour': 400, 'eggs': 4}, {}), 0)
