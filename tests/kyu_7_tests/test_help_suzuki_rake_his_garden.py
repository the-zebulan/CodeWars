import unittest

from katas.kyu_7.help_suzuki_rake_his_garden import rake_garden


class RakeGardenTestCase(unittest.TestCase):
    def test_equals_1(self):
        self.assertEqual(
            rake_garden('slug spider rock gravel gravel gravel gravel grave'
                        'l gravel gravel'),
            'gravel gravel rock gravel gravel gravel gravel gravel gravel g'
            'ravel'
        )

    def test_equals_2(self):
        self.assertEqual(
            rake_garden('gravel gravel gravel gravel gravel gravel gravel g'
                        'ravel gravel rock slug ant gravel gravel snail roc'
                        'k gravel gravel gravel gravel gravel gravel gravel'
                        ' slug gravel ant gravel gravel gravel gravel rock '
                        'slug gravel gravel gravel gravel gravel snail grav'
                        'el gravel rock gravel snail slug gravel gravel spi'
                        'der gravel gravel gravel gravel gravel gravel grav'
                        'el gravel moss gravel gravel gravel snail gravel g'
                        'ravel gravel ant gravel gravel moss gravel gravel '
                        'gravel gravel snail gravel gravel gravel gravel sl'
                        'ug gravel rock gravel gravel rock gravel gravel gr'
                        'avel gravel snail gravel gravel rock gravel gravel'
                        ' gravel gravel gravel spider gravel rock gravel gr'
                        'avel'),
            'gravel gravel gravel gravel gravel gravel gravel gravel gravel'
            ' rock gravel gravel gravel gravel gravel rock gravel gravel gr'
            'avel gravel gravel gravel gravel gravel gravel gravel gravel g'
            'ravel gravel gravel rock gravel gravel gravel gravel gravel gr'
            'avel gravel gravel gravel rock gravel gravel gravel gravel gra'
            'vel gravel gravel gravel gravel gravel gravel gravel gravel gr'
            'avel gravel gravel gravel gravel gravel gravel gravel gravel g'
            'ravel gravel gravel gravel gravel gravel gravel gravel gravel '
            'gravel gravel gravel gravel gravel gravel rock gravel gravel r'
            'ock gravel gravel gravel gravel gravel gravel gravel rock grav'
            'el gravel gravel gravel gravel gravel gravel rock gravel gravel')

    def test_equals_3(self):
        self.assertEqual(
            rake_garden('gravel gravel gravel gravel gravel gravel gravel g'
                        'ravel gravel rock slug ant gravel gravel snail roc'
                        'k gravel gravel gravel gravel gravel gravel gravel'
                        ' slug gravel ant gravel gravel gravel gravel rock '
                        'slug gravel gravel gravel gravel gravel snail grav'
                        'el gravel rock gravel snail slug gravel gravel spi'
                        'der gravel gravel gravel gravel gravel gravel grav'
                        'el gravel moss gravel gravel gravel snail gravel g'
                        'ravel gravel ant gravel gravel moss gravel gravel '
                        'gravel gravel snail gravel gravel gravel gravel sl'
                        'ug gravel rock gravel gravel rock gravel gravel gr'
                        'avel gravel snail gravel gravel rock gravel gravel'
                        ' gravel gravel gravel spider gravel rock gravel gr'
                        'avel'),
            'gravel gravel gravel gravel gravel gravel gravel gravel gravel'
            ' rock gravel gravel gravel gravel gravel rock gravel gravel gr'
            'avel gravel gravel gravel gravel gravel gravel gravel gravel g'
            'ravel gravel gravel rock gravel gravel gravel gravel gravel gr'
            'avel gravel gravel gravel rock gravel gravel gravel gravel gra'
            'vel gravel gravel gravel gravel gravel gravel gravel gravel gr'
            'avel gravel gravel gravel gravel gravel gravel gravel gravel g'
            'ravel gravel gravel gravel gravel gravel gravel gravel gravel '
            'gravel gravel gravel gravel gravel gravel rock gravel gravel r'
            'ock gravel gravel gravel gravel gravel gravel gravel rock grav'
            'el gravel gravel gravel gravel gravel gravel rock gravel gravel')


if __name__ == '__main__':
    unittest.main()
