import unittest

from katas.kyu_8.name_on_billboard import billboard


class BillboardTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(billboard("Jeong-Ho Aristotelis"), 600)

    def test_equal_2(self):
        self.assertEqual(billboard("Abishai Charalampos"), 570)

    def test_equal_3(self):
        self.assertEqual(billboard("Idwal Augustin"), 420)

    def test_equal_4(self):
        self.assertEqual(billboard("Hadufuns John", 20), 260)

    def test_equal_5(self):
        self.assertEqual(billboard("Zoroaster Donnchadh"), 570)

    def test_equal_6(self):
        self.assertEqual(billboard("Claude Miljenko"), 450)

    def test_equal_7(self):
        self.assertEqual(billboard("Werner Vigi", 15), 165)

    def test_equal_8(self):
        self.assertEqual(billboard("Anani Fridumar"), 420)

    def test_equal_9(self):
        self.assertEqual(billboard("Paolo Oli"), 270)

    def test_equal_10(self):
        self.assertEqual(billboard("Hjalmar Liupold", 40), 600)

    def test_equal_11(self):
        self.assertEqual(billboard("Simon Eadwulf"), 390)


if __name__ == '__main__':
    unittest.main()
