import unittest

from katas.kyu_7.where_is_wally import wheres_wally


class WhereIsWallyTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(wheres_wally(
            'Walley ,Wally -Wally ;Wally +Wally :Wally'), -1)

    def test_equals_2(self):
        self.assertEqual(wheres_wally(
            'Walley Wally, Wally- Wally: Wally+ Wally:'), 7)

    def test_equals_3(self):
        self.assertEqual(wheres_wally('.Wally'), -1)

    def test_equals_4(self):
        self.assertEqual(wheres_wally(''), -1)

    def test_equals_5(self):
        self.assertEqual(wheres_wally('WAlly'), -1)

    def test_equals_6(self):
        self.assertEqual(wheres_wally('wAlly'), -1)

    def test_equals_7(self):
        self.assertEqual(wheres_wally('Wally'), 0)

    def test_equals_8(self):
        self.assertEqual(wheres_wally('Where\'s Wally'), 8)

    def test_equals_9(self):
        self.assertEqual(wheres_wally('Wallyd'), -1)

    def test_equals_10(self):
        self.assertEqual(wheres_wally('It\'s Wally\'s.'), 5)


if __name__ == '__main__':
    unittest.main()
