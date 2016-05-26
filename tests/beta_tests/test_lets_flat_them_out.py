import unittest

from katas.beta.lets_flat_them_out import flatten


class FlattenTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(flatten({'key': 'value'}), {'key': 'value'})

    def test_equal_2(self):
        self.assertEqual(flatten({
            'key': {'deeper': {'more': {'enough': 'value'}}}
        }), {'key/deeper/more/enough': 'value'}
        )

    def test_equal_3(self):
        self.assertEqual(flatten({'empty': {}}), {'empty': ''})

    def test_equal_4(self):
        self.assertEqual(flatten({
            'name': {'first': 'One', 'last': 'Drone'},
            'job': 'scout',
            'recent': {},
            'additional': {'place': {'zone': '1', 'cell': '2'}}
        }), {
            'name/first': 'One',
            'name/last': 'Drone',
            'job': 'scout',
            'recent': '',
            'additional/place/zone': '1',
            'additional/place/cell': '2'
        })

    def test_equal_5(self):
        self.assertEqual(flatten({
            'job': {'1': 'scout', '2': 'worker', '3': 'writer',
                    '4': 'reader', '5': 'learner'},
            'name': {'nick': {}, 'last': 'Drone', 'first': 'Second'},
            'recent': {
                'places': {
                    'earth': {'NP': '', 'NY': '2017', 'Louvre': '2015'}
                },
                'times': {'XX': {'1964': 'Yes'}, 'XXI': {'2064': 'Nope'}}
            }
        }), {
            'job/1': 'scout', 'recent/places/earth/NY': '2017',
            'job/3': 'writer', 'job/2': 'worker', 'job/5': 'learner',
            'job/4': 'reader', 'recent/places/earth/NP': '',
            'recent/places/earth/Louvre': '2015',
            'recent/times/XX/1964': 'Yes', 'recent/times/XXI/2064': 'Nope',
            'name/first': 'Second', 'name/last': 'Drone', 'name/nick': ''
        })

    def test_equal_6(self):
        self.assertEqual(flatten({
            'Hm': {'What': {'is': {'here': {'?': {}}}}}
        }), {'Hm/What/is/here/?': ''}
        )

    def test_equal_7(self):
        self.assertEqual(flatten({
            'flat': 'yep', 'who': 'iam', 'root': 'yep'
        }), {'flat': 'yep', 'who': 'iam', 'root': 'yep'}
        )

    def test_equal_8(self):
        self.assertEqual(flatten({
            '1': 'X', '3': {
                '31': {'312': 'V'}, '34': {'345': {'3458': {'34580': 'X'}}}
            }
        }), {'1': 'X', '3/31/312': 'V', '3/34/345/3458/34580': 'X'}
        )

    def test_equal_9(self):
        self.assertEqual(flatten({
            'glossary': {
                'GlossDiv': {
                    'GlossList': {
                        'GlossEntry': {
                            'GlossDef': {
                                'GlossSeeAlso': {'1': 'GML', '2': 'XML'},
                                'para': 'A meta-markup language, used to cr'
                                        'eate markup languages such as DocB'
                                        'ook.'
                            },
                            'GlossSee': 'markup',
                            'Acronym': 'SGML',
                            'GlossTerm': 'Standard Generalized Markup Langu'
                                         'age',
                            'Abbrev': 'ISO 8879:1986',
                            'SortAs': 'SGML',
                            'ID': 'SGML'
                        }
                    }, 'title': 'S'
                }, 'title': 'example glossary'
            },
            'source': 'http://json.org/example'
        }), {
            'glossary/GlossDiv/GlossList/GlossEntry/GlossDef/para':
                'A meta-markup language, used to create markup languages su'
                'ch as DocBook.',
            'glossary/title': 'example glossary',
            'glossary/GlossDiv/GlossList/GlossEntry/Abbrev': 'ISO 8879:1986',
            'glossary/GlossDiv/GlossList/GlossEntry/SortAs': 'SGML',
            'glossary/GlossDiv/GlossList/GlossEntry/Acronym': 'SGML',
            'glossary/GlossDiv/GlossList/GlossEntry/GlossTerm':
                'Standard Generalized Markup Language',
            'glossary/GlossDiv/title': 'S',
            'source': 'http://json.org/example',
            'glossary/GlossDiv/GlossList/GlossEntry/GlossDef/GlossSeeAlso/2':
                'XML',
            'glossary/GlossDiv/GlossList/GlossEntry/ID': 'SGML',
            'glossary/GlossDiv/GlossList/GlossEntry/GlossDef/GlossSeeAlso/1':
                'GML',
            'glossary/GlossDiv/GlossList/GlossEntry/GlossSee': 'markup'
        })


if __name__ == '__main__':
    unittest.main()
