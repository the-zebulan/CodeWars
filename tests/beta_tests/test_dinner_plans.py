import unittest

from katas.beta.dinner_plans import common_ground


class CommonGroundTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(common_ground(
            'eat chicken', 'eat chicken and rice'
        ), 'eat chicken')

    def test_equal_2(self):
        self.assertEqual(common_ground(
            'eat a burger and drink a coke', 'drink a coke'
        ), 'drink a coke')

    def test_equal_3(self):
        self.assertEqual(common_ground(
            'i like turtles', 'what are you talking about'
        ), 'death')

    def test_equal_4(self):
        self.assertEqual(common_ground('aa bb', 'aa bb cc'), 'aa bb')

    def test_equal_5(self):
        self.assertEqual(common_ground('aa bb cc', 'bb cc'), 'bb cc')

    def test_equal_6(self):
        self.assertEqual(common_ground('aa bb cc', 'bb cc bb aa'), 'bb cc aa')

    def test_equal_7(self):
        self.assertEqual(common_ground('aa bb', 'cc dd'), 'death')

    def test_equal_8(self):
        self.assertEqual(common_ground('aa bb', ''), 'death')

    def test_equal_9(self):
        self.assertEqual(common_ground('', 'cc dd'), 'death')

    def test_equal_10(self):
        self.assertEqual(common_ground('', ''), 'death')


if __name__ == '__main__':
    unittest.main()
