from re import compile, match

REGEX = compile(r'(http[s]*://)?(www.)?(?P<domain>[\w-]+)\.')


def domain_name(url):
    return match(REGEX, url).group('domain')
