import unittest

from katas.beta.exclusive_presentations import presentation_agenda


class PresentationAgendaTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(presentation_agenda([
            {'person': 'Abe', 'dest': ['Singapore', 'Dubai']},
            {'person': 'Brad', 'dest': ['Paris', 'Dubai']}
        ]), [{'dest': ['Singapore'], 'person': 'Abe'},
             {'dest': ['Paris'], 'person': 'Brad'}])

    def test_equal_2(self):
        self.assertEqual(presentation_agenda([
            {'person': 'Abe', 'dest': ['London', 'Dubai']},
            {'person': 'Bond', 'dest': ['Melbourne', 'Dubai']}
        ]), [{'person': 'Abe', 'dest': ['London']},
             {'person': 'Bond', 'dest': ['Melbourne']}])

    def test_equal_3(self):
        self.assertEqual(presentation_agenda([
            {'person': 'Abe', 'dest': ['Dubai']},
            {'person': 'Brad', 'dest': ['Dubai']}
        ]), [])

    def test_equal_4(self):
        self.assertEqual(presentation_agenda([
            {'person': 'Abe', 'dest': ['London', 'Dubai']},
            {'person': 'Bond', 'dest': ['Melbourne', 'Dubai']},
            {'person': 'Carrie', 'dest': ['Melbourne']},
            {'person': 'Damu', 'dest': ['Melbourne', 'Dubai', 'Paris']}
        ]), [{'person': 'Abe',  'dest': ['London']},
             {'person': 'Damu', 'dest': ['Paris']}])
