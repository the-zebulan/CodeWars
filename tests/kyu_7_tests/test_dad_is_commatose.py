import unittest

from kyu_7.dad_is_commatose import dad_filter


class DadFilterTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(dad_filter('all this,,,, used to be trees,,,,,,'),
                         'all this, used to be trees')

    def test_equals_2(self):
        self.assertEqual(dad_filter('Listen,,,, kid,,,,,,'), 'Listen, kid')

    def test_equals_3(self):
        self.assertEqual(dad_filter(
            'Luke,,,,,,,,, I am your father,,,,,,,,,  '
        ), 'Luke, I am your father')

    def test_equals_4(self):
        self.assertEqual(dad_filter(
            'i,, don\'t believe this round earth,,, show me evadence!!'
        ), 'i, don\'t believe this round earth, show me evadence!!')

    def test_equals_5(self):
        self.assertEqual(dad_filter(
            'Dead or alive,,,, you\'re coming with me,,,   '
        ), 'Dead or alive, you\'re coming with me')


if __name__ == '__main__':
    unittest.main()
