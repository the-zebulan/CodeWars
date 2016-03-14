import unittest

from katas.beta.string_incrementer import increment_string


class IncrementStringTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(increment_string('foo'), 'foo1')

    def test_equals_2(self):
        self.assertEqual(increment_string('foobar23'), 'foobar24')

    def test_equals_3(self):
        self.assertEqual(increment_string('foo0042'), 'foo0043')

    def test_equals_4(self):
        self.assertEqual(increment_string('foo9'), 'foo10')

    def test_equals_5(self):
        self.assertEqual(increment_string('foo099'), 'foo100')

    def test_equals_6(self):
        self.assertEqual(increment_string('foobar00'), 'foobar01')

    def test_equals_7(self):
        self.assertEqual(increment_string('foobar001'), 'foobar002')

    def test_equals_8(self):
        self.assertEqual(increment_string('foobar1'), 'foobar2')

    def test_equals_9(self):
        self.assertEqual(increment_string('foobar99'), 'foobar100')

    def test_equals_10(self):
        self.assertEqual(increment_string(''), '1')


if __name__ == '__main__':
    unittest.main()
