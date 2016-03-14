import unittest

from katas.kyu_7.simple_template import create_template


class TemplateTestCase(unittest.TestCase):
    def setUp(self):
        self.template = create_template('{{name}} likes {{animalType}}')
        self.template2 = create_template('{{first}} {{last}}')

    def test_equals(self):
        self.assertEqual(
            self.template(name='John', animalType='dogs'), 'John likes dogs'
        )

    def test_equals_2(self):
        self.assertEqual(
            self.template2(first='Smitty', last='Bacall'), 'Smitty Bacall'
        )

    def test_equals_3(self):
        self.assertEqual(
            self.template2(first='Smitty', other='other'), 'Smitty '
        )


if __name__ == '__main__':
    unittest.main()
