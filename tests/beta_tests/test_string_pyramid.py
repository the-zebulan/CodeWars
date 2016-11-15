import unittest
from textwrap import dedent

from katas.beta.string_pyramid import (
    count_all_characters_of_the_pyramid,
    count_visible_characters_of_the_pyramid,
    watch_pyramid_from_above,
    watch_pyramid_from_the_side
)


class StringPyramidTestCase(unittest.TestCase):
    def test_is_none_1(self):
        self.assertIsNone(watch_pyramid_from_the_side(None))

    def test_is_none_2(self):
        self.assertIsNone(watch_pyramid_from_above(None))

    def test_equal_1(self):
        self.assertEqual(count_visible_characters_of_the_pyramid(None), -1)

    def test_equal_2(self):
        self.assertEqual(count_all_characters_of_the_pyramid(None), -1)

    def test_equal_3(self):
        self.assertEqual(watch_pyramid_from_the_side(''), '')

    def test_equal_4(self):
        self.assertEqual(watch_pyramid_from_above(''), '')

    def test_equal_5(self):
        self.assertEqual(count_visible_characters_of_the_pyramid(''), -1)

    def test_equal_6(self):
        self.assertEqual(count_all_characters_of_the_pyramid(''), -1)

    def test_equal_7(self):
        characters = '*#'
        expected_watch_from_side = dedent('''\
             # 
            ***''')
        expected_watch_from_above = dedent('''\
            ***
            *#*
            ***''')
        self.assertEqual(
            count_visible_characters_of_the_pyramid(characters), 9
        )
        self.assertEqual(count_all_characters_of_the_pyramid(characters), 10)
        self.assertEqual(watch_pyramid_from_the_side(characters),
                         expected_watch_from_side)
        self.assertEqual(watch_pyramid_from_above(characters),
                         expected_watch_from_above)

    def test_equal_8(self):
        characters = 'abc'
        expected_watch_from_side = dedent('''\
              c  
             bbb 
            aaaaa''')
        expected_watch_from_above = dedent('''\
            aaaaa
            abbba
            abcba
            abbba
            aaaaa''')
        self.assertEqual(
            count_visible_characters_of_the_pyramid(characters), 25
        )
        self.assertEqual(count_all_characters_of_the_pyramid(characters), 35)
        self.assertEqual(watch_pyramid_from_the_side(characters),
                         expected_watch_from_side)
        self.assertEqual(watch_pyramid_from_above(characters),
                         expected_watch_from_above)

    def test_equal_9(self):
        characters = 'aaa'
        expected_watch_from_side = dedent('''\
              a  
             aaa 
            aaaaa''')
        expected_watch_from_above = dedent('''\
            aaaaa
            aaaaa
            aaaaa
            aaaaa
            aaaaa''')
        self.assertEqual(
            count_visible_characters_of_the_pyramid(characters), 25
        )
        self.assertEqual(count_all_characters_of_the_pyramid(characters), 35)
        self.assertEqual(watch_pyramid_from_the_side(characters),
                         expected_watch_from_side)
        self.assertEqual(watch_pyramid_from_above(characters),
                         expected_watch_from_above)

    def test_equal_10(self):
        characters = '54321'
        expected_watch_from_side = dedent('''\
                1    
               222   
              33333  
             4444444 
            555555555''')

        expected_watch_from_above = dedent('''\
            555555555
            544444445
            543333345
            543222345
            543212345
            543222345
            543333345
            544444445
            555555555''')
        self.assertEqual(
            count_visible_characters_of_the_pyramid(characters), 81
        )
        self.assertEqual(count_all_characters_of_the_pyramid(characters), 165)
        self.assertEqual(watch_pyramid_from_the_side(characters),
                         expected_watch_from_side)
        self.assertEqual(watch_pyramid_from_above(characters),
                         expected_watch_from_above)
