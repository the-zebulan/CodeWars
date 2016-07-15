import unittest

from katas.kyu_7.green_glass_door import step_through_with


class StepThroughWithTestCase(unittest.TestCase):
    def test_true(self):
        self.assertTrue(step_through_with('moon'))

    def test_true_2(self):
        self.assertTrue(step_through_with('glasses'))

    def test_true_3(self):
        self.assertTrue(step_through_with('free'))

    def test_false(self):
        self.assertFalse(step_through_with('test'))

    def test_false_2(self):
        self.assertFalse(step_through_with('airplane'))

    def test_false_3(self):
        self.assertFalse(step_through_with('branch'))
