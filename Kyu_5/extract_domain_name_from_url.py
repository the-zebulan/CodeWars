from re import compile, match

REGEX = compile(r'(http[s]*://)?(www.)?(?P<domain>[\w-]+)\.')


def domain_name(url):
    return match(REGEX, url).group('domain')


assert domain_name('http://github.com/carbonfive/raygun') == 'github'
assert domain_name('http://www.zombie-bites.com') == 'zombie-bites'
assert domain_name('https://www.cnet.com') == 'cnet'
assert domain_name('www.xakep.ru') == 'xakep'
