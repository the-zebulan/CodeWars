import unittest

from katas.beta.loose_change import loose_change


class LooseChangeTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(loose_change(56), {'Nickels': 1, 'Pennies': 1,
                                            'Dimes': 0, 'Quarters': 2})

    def test_equals_2(self):
        self.assertEqual(loose_change(-435), {'Nickels': 0, 'Pennies': 0,
                                              'Dimes': 0, 'Quarters': 0})

    def test_equals_3(self):
        self.assertEqual(loose_change(4.935), {'Nickels': 0, 'Pennies': 4,
                                               'Dimes': 0, 'Quarters': 0})

    def test_equals_4(self):
        self.assertEqual(loose_change(29), {'Nickels': 0, 'Pennies': 4,
                                            'Dimes': 0, 'Quarters': 1})

    def test_equals_5(self):
        self.assertEqual(loose_change(91), {'Nickels': 1, 'Pennies': 1,
                                            'Dimes': 1, 'Quarters': 3})

    def test_equals_6(self):
        self.assertEqual(loose_change(0), {'Nickels': 0, 'Pennies': 0,
                                           'Dimes': 0, 'Quarters': 0})

    def test_equals_7(self):
        self.assertEqual(loose_change(-2), {'Nickels': 0, 'Pennies': 0,
                                            'Dimes': 0, 'Quarters': 0})

    def test_equals_8(self):
        self.assertEqual(loose_change(3.9), {'Nickels': 0, 'Pennies': 3,
                                             'Dimes': 0, 'Quarters': 0})


if __name__ == '__main__':
    unittest.main()
