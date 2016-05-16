import unittest

from katas.beta.how_many_minutes import date_to_mins


class DateToMinutesTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(date_to_mins('02/10/2016'), 59040)

    def test_equals_2(self):
        self.assertEqual(date_to_mins('02/29/2016'), 86400)

    def test_equals_3(self):
        self.assertEqual(date_to_mins('04/21/2016'), 161280)

    def test_equals_4(self):
        self.assertEqual(date_to_mins('05/31/2016'), 218880)

    def test_equals_5(self):
        self.assertEqual(date_to_mins('invalid date!'), -1)


if __name__ == '__main__':
    unittest.main()
