from itertools import izip_longest


def next_version(version):
    dots = '.' * version.count('.')
    num = str(int(''.join(version.split('.'))) + 1)
    return ''.join(''.join(a) for a in
                   izip_longest(reversed(num), dots, fillvalue=''))[::-1]
