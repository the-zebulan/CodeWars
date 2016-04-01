import unittest

from katas.kyu_7.conference_traveller import conference_picker


class ConferencePickerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(conference_picker(
            [], ['Philadelphia', 'Osaka', 'Tokyo', 'Melbourne']
            ), 'Philadelphia'
        )

    def test_equals_2(self):
        self.assertEqual(
            conference_picker([], ['Brussels', 'Madrid', 'London']),
            'Brussels'
        )

    def test_equals_3(self):
        self.assertEqual(conference_picker([], ['Sydney', 'Tokyo']), 'Sydney')

    def test_equals_4(self):
        self.assertEqual(conference_picker(
            ['London', 'Berlin', 'Mexico City', 'Melbourne', 'Buenos Aires',
             'Hong Kong', 'Madrid', 'Paris'], ['Berlin', 'Melbourne']
            ), 'No worthwhile conferences this year!'
        )

    def test_equals_5(self):
        self.assertEqual(conference_picker(
            ['Beijing', 'Johannesburg', 'Sydney', 'Philadelphia', 'Hong Kong',
             'Stockholm', 'Chicago', 'Seoul', 'Mexico City', 'Berlin'],
            ['Stockholm', 'Berlin', 'Chicago']
            ), 'No worthwhile conferences this year!'
        )

    def test_equals_6(self):
        self.assertEqual(conference_picker(['Rome'], ['Rome']),
                         'No worthwhile conferences this year!')

    def test_equals_7(self):
        self.assertEqual(conference_picker(['Milan'], ['London']), 'London')

    def test_equals_8(self):
        self.assertEqual(conference_picker(
            ['Mexico City', 'Dubai', 'Philadelphia', 'Madrid', 'Houston',
             'Chicago', 'Delhi', 'Seoul', 'Mumbai', 'Lisbon', 'Hong Kong',
             'Brisbane', 'Stockholm', 'Tokyo', 'San Francisco',
             'Rio De Janeiro'], ['Lisbon', 'Mexico City']
            ), 'No worthwhile conferences this year!'
        )

    def test_equals_9(self):
        self.assertEqual(conference_picker(
            ['Gatlantis', 'Baldur\'s Gate', 'Gotham City', 'Mystara',
             'Washinkyo', 'Central City'],
            ['Mystara', 'Gatlantis', 'MegaTokyo', 'Genosha', 'Central City',
             'Washinkyo', 'Gotham City', 'King\'s Landing', 'Waterdeep']
            ), 'MegaTokyo'
        )

    def test_equals_10(self):
        self.assertEqual(conference_picker(
            ['Thay', 'Camelot'], ['Waterdeep', 'Washinkyo']
            ), 'Waterdeep'
        )


if __name__ == '__main__':
    unittest.main()
