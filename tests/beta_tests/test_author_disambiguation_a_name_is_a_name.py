import unittest

from katas.beta.author_disambiguation_a_name_is_a_name import could_be


class CouldBeTestCase(unittest.TestCase):
    def test_true_1(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Carlos Ray Norris'))

    def test_true_2(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Carlos Ray'))

    def test_true_3(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Ray Norris'))

    def test_true_4(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Carlos Norris'))

    def test_true_5(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Norris'))

    def test_true_6(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Carlos'))

    def test_true_7(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Norris Carlos'))

    def test_true_8(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'carlos ray norris'))

    def test_true_9(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Norris! ?ray'))

    def test_true_10(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Carlos. Ray; Norris,'))

    def test_true_11(self):
        self.assertTrue(could_be('Carlos Ray Norris', 'Carlos:Ray Norris'))

    def test_true_12(self):
        self.assertTrue(could_be('Carlos-Ray Norris', 'Carlos-Ray Norris:'))

    def test_true_13(self):
        self.assertTrue(could_be('Carlos Ray-Norris', 'Carlos? Ray-Norris'))

    def test_false_1(self):
        self.assertFalse(could_be('Carlos Ray Norris', 'Carlos Ray Norr'))

    def test_false_2(self):
        self.assertFalse(could_be('Carlos Ray Norris', 'Ra Norris'))

    def test_false_3(self):
        self.assertFalse(could_be('', 'C'))

    def test_false_4(self):
        self.assertFalse(could_be('', ''))

    def test_false_5(self):
        self.assertFalse(could_be('Carlos Ray Norris', ' '))

    def test_false_6(self):
        self.assertFalse(could_be('Carlos-Ray Norris', 'Carlos Ray-Norris'))

    def test_false_7(self):
        self.assertFalse(could_be('Carlos Ray Norris', 'Carlos-Ray Norris'))

    def test_false_8(self):
        self.assertFalse(could_be('Carlos-Ray Norris', 'Carlos Ray-Norris'))

    def test_false_9(self):
        self.assertFalse(could_be('Carlos Ray Norris', 'Carlos Ray-Norris'))

    def test_false_10(self):
        self.assertFalse(could_be('Carlos Ray', 'Carlos Ray Norris'))

    def test_false_11(self):
        self.assertFalse(could_be('Carlos', 'Carlos Ray Norris'))
