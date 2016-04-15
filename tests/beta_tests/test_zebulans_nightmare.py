import unittest

from katas.beta.zebulans_nightmare import zebulansNightmare


class ZebulanTestCase(unittest.TestCase):
    def test_equal_1(self):
        self.assertEqual(zebulansNightmare('camel_case'), 'camelCase')

    def test_equal_2(self):
        self.assertEqual(zebulansNightmare('mark_as_issue'), 'markAsIssue')

    def test_equal_3(self):
        self.assertEqual(
            zebulansNightmare('copy_paste_pep8'), 'copyPastePep8'
        )

    def test_equal_4(self):
        self.assertEqual(zebulansNightmare('goto_next_kata'), 'gotoNextKata')

    def test_equal_5(self):
        self.assertEqual(zebulansNightmare('repeat'), 'repeat')


if __name__ == '__main__':
    unittest.main()
