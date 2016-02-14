from collections import defaultdict
from re import compile, match

REGEX = compile(r'(?P<num>\d+) (?P<adr>.+) (?P<st_zip>[A-Z]{2} \d{5})')


def travel(addresses, zipcode):
    by_zipcode = defaultdict(lambda: defaultdict(list))
    for address in addresses.split(','):
        m = match(REGEX, address).groupdict()
        by_zipcode[m['st_zip']]['adr'].append(m['adr'])
        by_zipcode[m['st_zip']]['num'].append(m['num'])
    result = by_zipcode[zipcode]
    return '{}:{}/{}'\
        .format(zipcode, ','.join(result['adr']), ','.join(result['num']))


r = '123 Main Street St. Louisville OH 43071,' \
    '432 Main Long Road St. Louisville OH 43071,' \
    '786 High Street Pollocksville NY 56432'
assert travel(r, 'OH 43071') == \
    'OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432'
assert travel(r, 'NY 56432') == 'NY 56432:High Street Pollocksville/786'
assert travel(r, 'NY 5643') == 'NY 5643:/'
