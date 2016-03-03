import unittest

from Kyu_4.human_readable_duration_format import format_duration


class FormatDurationTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(format_duration(1), '1 second')

    def test_equals_2(self):
        self.assertEqual(format_duration(62), '1 minute and 2 seconds')

    def test_equals_3(self):
        self.assertEqual(format_duration(120), '2 minutes')

    def test_equals_4(self):
        self.assertEqual(format_duration(3600), '1 hour')

    def test_equals_5(self):
        self.assertEqual(format_duration(3662),
                         '1 hour, 1 minute and 2 seconds')


if __name__ == '__main__':
    unittest.main()
