import unittest

from kyu_7.find_an_employees_role_in_the_company import find_employees_role


class FindEmployeesRoleTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(find_employees_role('Dipper Pines'),
                         'Does not work here!')

    def test_equals_2(self):
        self.assertEqual(find_employees_role('Morty Smith'), 'Truck Driver')

    def test_equals_3(self):
        self.assertEqual(find_employees_role('Anna Bell'), 'Admin')


if __name__ == '__main__':
    unittest.main()
