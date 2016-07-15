import unittest

from katas.kyu_5.extract_domain_name_from_url import domain_name


class DomainNameTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(domain_name(
            'http://github.com/carbonfive/raygun'), 'github')

    def test_equals_2(self):
        self.assertEqual(domain_name(
            'http://www.zombie-bites.com'), 'zombie-bites')

    def test_equals_3(self):
        self.assertEqual(domain_name('https://www.cnet.com'), 'cnet')

    def test_equals_4(self):
        self.assertEqual(domain_name('www.xakep.ru'), 'xakep')
