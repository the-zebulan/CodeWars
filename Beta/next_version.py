from itertools import izip_longest


def next_version(version):
    dots = '.' * version.count('.')
    num = str(int(''.join(version.split('.'))) + 1)
    return ''.join(''.join(a) for a in
                   izip_longest(reversed(num), dots, fillvalue=''))[::-1]


assert next_version('1.2.3') == '1.2.4'
assert next_version('0.9.9') == '1.0.0'
assert next_version('1') == '2'
assert next_version('1.2.3.4.5.6.7.8') == '1.2.3.4.5.6.7.9'
assert next_version('9.9') == '10.0'
