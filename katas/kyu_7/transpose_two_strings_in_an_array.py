from itertools import izip_longest


def transpose_two_strings(arr):
    output = '{} {}'.format
    return '\n'.join(output(*a) for a in izip_longest(*arr, fillvalue=' '))
