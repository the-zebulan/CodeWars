import unittest

from katas.kyu_8.adam_and_eve import God, Man


class AdamAndEveTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertIsInstance(God()[0], Man)
