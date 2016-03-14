import unittest

from katas.beta.pythons_dynamic_classes_1 import class_name_changer


class ClassNameChangerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(str(MyClass), '<class \'tests.beta_tests.test_pythons_dyna'
                                       'mic_classes_1.MyClass\'>')

    def test_equals_2(self):
        class_name_changer(MyClass, 'UsefulClass')
        self.assertEqual(str(MyClass), '<class \'tests.beta_tests.test_pythons_dyna'
                                       'mic_classes_1.UsefulClass\'>')

    def test_equals_3(self):
        class_name_changer(MyClass, 'SecondUsefulClass')
        self.assertEqual(str(MyClass), '<class \'tests.beta_tests.test_pythons_dyna'
                                       'mic_classes_1.SecondUsefulClass\'>')


class MyClass(object):
    def __str__(self):
        return str(type(self))


if __name__ == '__main__':
    unittest.main()
