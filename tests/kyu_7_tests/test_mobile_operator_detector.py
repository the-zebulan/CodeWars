import unittest

from katas.kyu_7.mobile_operator_detector import detect_operator


class DetectOperatorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(detect_operator(80661111841), 'MTS')

    def test_equals_2(self):
        self.assertEqual(detect_operator(80671991111), 'Kyivstar')

    def test_equals_3(self):
        self.assertEqual(detect_operator(80631551111), 'Life:)')

    def test_equals_4(self):
        self.assertEqual(detect_operator(80931551111), 'Life:)')

    def test_equals_5(self):
        self.assertEqual(detect_operator(80111551111), 'no info')
