from itertools import izip_longest


def combine_strings(*args):
    return ''.join(''.join(a) for a in izip_longest(*args, fillvalue=''))
