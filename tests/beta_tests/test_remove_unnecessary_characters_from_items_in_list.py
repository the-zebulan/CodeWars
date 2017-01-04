import unittest

from katas.beta.remove_unnecessary_characters_from_items_in_list import (
    remove_char)


class RemoveCharTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(remove_char(
            ['$56.6xs4', '{$33ae.5(9', '$29.4e9', '%$9|4d.20', 'AAA$4r R4.94']
        ), ['$56.64', '$33.59', '$29.49', '$94.20', '$44.94'])

    def test_equal_2(self):
        self.assertEqual(remove_char(
            ['%%$9p2. 42', '"e"$15o.4/d9', '$29.29', ',$,59,.,25', 'E$5.0O0']
        ), ['$92.42', '$15.49', '$29.29', '$59.25', '$5.00'])
