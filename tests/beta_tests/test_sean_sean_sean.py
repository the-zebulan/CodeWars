import unittest

from katas.beta.sean_sean_sean import sean


class SeanTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(sean("Hello its me"), "Ohhhhh it's Sean!")

    def test_equal_2(self):
        self.assertEqual(sean(
            "Compare us to the world, the outlier, the doubtfire!"
        ), "Ohhhhh it's Sean! Sean! Sean! Sean! Sean! Sean! Sean!")

    def test_equal_3(self):
        self.assertEqual(sean(
            "    Nothing is promised,    but what if my gas is the best Dou"
            "bt what brother ohhhhhhhh     "
        ), "Ohhhhh it's Sean! Sean! Sean! Sean! Sean! Sean! Sean! Sean! Sea"
           "n! SEAN! Sean! Sean! Sean!")

    def test_equal_4(self):
        self.assertEqual(sean("ohh"), "Ohhhhh it's Sean!")

    def test_equal_5(self):
        self.assertEqual(sean(7777), "Boo! Not a string, boo!")

    def test_equal_6(self):
        self.assertEqual(sean(""), "Ohhhhh it's Sean!")

    def test_equal_7(self):
        self.assertEqual(sean("^^ ^^^"), "Ohhhhh it's Sean!")

    def test_equal_8(self):
        self.assertEqual(sean([]), "Boo! Not a string, boo!")

    def test_equal_9(self):
        self.assertEqual(sean("Hello my brother hello my ^^^ & *"),
                         "Ohhhhh it's Sean! Sean! Sean! SEAN! SEAN! SEAN!")

    def test_equal_10(self):
        self.assertEqual(sean("SEAN SEAN SEAN SEAN SEAN\nSEAN"),
                         "Ohhhhh it's SEAN! SEAN! SEAN! SEAN!")


if __name__ == '__main__':
    unittest.main()
