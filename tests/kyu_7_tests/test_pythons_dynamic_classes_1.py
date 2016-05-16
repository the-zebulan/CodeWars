import unittest

from katas.kyu_7.pythons_dynamic_classes_1 import class_name_changer


class ClassNameChangerTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(str(MyClass),
                         '<class \'tests.kyu_7_tests.test_pythons_dynamic_c'
                         'lasses_1.MyClass\'>')

    def test_equals_2(self):
        class_name_changer(MyClass, 'UsefulClass')
        self.assertEqual(str(MyClass),
                         '<class \'tests.kyu_7_tests.test_pythons_dynamic_c'
                         'lasses_1.UsefulClass\'>')

    def test_equals_3(self):
        class_name_changer(MyClass, 'SecondUsefulClass')
        self.assertEqual(str(MyClass),
                         '<class \'tests.kyu_7_tests.test_pythons_dynamic_c'
                         'lasses_1.SecondUsefulClass\'>')

    def test_raises_1(self):
        self.assertRaises(NameError, class_name_changer, MyClass, 'bad_name')

    def test_raises_2(self):
        self.assertRaises(NameError, class_name_changer, MyClass, '!@#$%%^')


class MyClass(object):
    def __str__(self):
        return str(type(self))


if __name__ == '__main__':
    unittest.main()
