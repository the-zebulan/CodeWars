import unittest

from Kyu_4.breadcrumb_generator import generate_bc


class BreadcrumbGeneratorTestCase(unittest.TestCase):
    def test_equals(self):
        self.assertEqual(generate_bc(
            'https://codewars.com/insider-the-the-transmutation-from-and/wan'
            'ted/diplomatic-bioengineering/at-from-surfer-cauterization-skin',
            ' - '),
            '<a href="/">HOME</a> - <a href="/insider-the-the-transmutation-'
            'from-and/">IT</a> - <a href="/insider-the-the-transmutation-fro'
            'm-and/wanted/">WANTED</a> - <a href="/insider-the-the-transmuta'
            'tion-from-and/wanted/diplomatic-bioengineering/">DIPLOMATIC BIO'
            'ENGINEERING</a> - <span class="active">SCS</span>')

    def test_equals_2(self):
        self.assertEqual(generate_bc('http://www.agcpartners.co.uk', ' % '),
                         '<span class="active">HOME</span>')

    def test_equals_3(self):
        self.assertEqual(generate_bc(
            'https://www.agcpartners.co.uk/', ' >>> '),
            '<span class="active">HOME</span>')

    def test_equals_4(self):
        self.assertEqual(generate_bc('www.agcpartners.co.uk', ' # '),
                         '<span class="active">HOME</span>')

    def test_equals_5(self):
        self.assertEqual(generate_bc('www.agcpartners.co.uk/', ' * '),
                         '<span class="active">HOME</span>')

    def test_equals_6(self):
        self.assertEqual(generate_bc(
            "mysite.com/pictures/holidays.html", " : "),
            '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <spa'
            'n class="active">HOLIDAYS</span>')

    def test_equals_7(self):
        self.assertEqual(generate_bc(
            "www.codewars.com/users/GiacomoSorbi", " / "),
            '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span clas'
            's="active">GIACOMOSORBI</span>')

    def test_equals_8(self):
        self.assertEqual(generate_bc(
            "www.microsoft.com/docs/index.htm", " * "),
            '<a href="/">HOME</a> * <span class="active">DOCS</span>')

    def test_equals_9(self):
        self.assertEqual(generate_bc(
            "mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example"
            "/example.htm", " > "),
            '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-'
            'yet-meaningful-example/">VLUMSYME</a> > <span class="active">EX'
            'AMPLE</span>')

    def test_equals_10(self):
        self.assertEqual(generate_bc(
            "www.very-long-site_name-to-make-a-silly-yet-meaningful-example."
            "com/users/giacomo-sorbi", " + "),
            '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span clas'
            's="active">GIACOMO SORBI</span>')

    def test_equals_11(self):
        self.assertEqual(generate_bc('www.microsoft.com/important/confidenti'
                                     'al/docs/index.htm#top', ' * '),
                         '<a href="/">HOME</a> * <a href="/important/">IMPOR'
                         'TANT</a> * <a href="/important/confidential/">CONF'
                         'IDENTIAL</a> * <span class="active">DOCS</span>')


if __name__ == '__main__':
    unittest.main()
