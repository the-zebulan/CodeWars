import unittest

from katas.beta.sum_of_values_from_1_to_n_inclusive import total


class SumFromOneToNTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(total(10), 55)

    def test_equal_2(self):
        self.assertEqual(total(123), 7626)

    def test_equal_3(self):
        self.assertEqual(total(1000), 500500)

    def test_equal_4(self):
        self.assertEqual(total(54321), 1475412681)

    def test_equal_5(self):
        self.assertEqual(total(12345), 76205685)

    def test_equal_6(self):
        self.assertEqual(total(35765), 639585495)

    def test_equal_7(self):
        self.assertEqual(total(98765), 4877311995)

    def test_equal_8(self):
        self.assertEqual(total(56478), 1594910481)

    def test_equal_9(self):
        self.assertEqual(total(1111111), 617284382716)

    def test_equal_10(self):
        self.assertEqual(total(2222222), 2469136419753)

    def test_equal_11(self):
        self.assertEqual(total(3333333), 5555556111111)

    def test_equal_12(self):
        self.assertEqual(total(4444444), 9876543456790)

    def test_equal_13(self):
        self.assertEqual(total(5555555), 15432098456790)

    def test_equal_14(self):
        self.assertEqual(total(6666666), 22222221111111)

    def test_equal_15(self):
        self.assertEqual(total(7777777), 30246911419753)
