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
