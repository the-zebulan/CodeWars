import unittest

from katas.beta.find_jon_snow_parents import jonSnowParents


class JonSnowParentsTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(jonSnowParents('Robert Baratheon', 'Catelyn Stark'),
                         'Jon Snow, you know nothing')

    def test_equal_2(self):
        self.assertEqual(jonSnowParents('Lyanna Stark', 'Rhaegar Targaryen'),
                         'Jon Snow, you know nothing')

    def test_equal_3(self):
        self.assertEqual(jonSnowParents('Barack Obama', 'Lady Gaga'),
                         'Jon Snow, you know nothing')

    def test_equal_4(self):
        self.assertEqual(jonSnowParents('Rhaegar Targaryen', 'Lyanna Stark'),
                         'Jon Snow you deserve the throne')

    def test_not_equal_1(self):
        self.assertNotEqual(
            jonSnowParents('Rhaegar Targaryen', 'Lyanna Stark'),
            'Jon Snow, you know nothing'
        )
