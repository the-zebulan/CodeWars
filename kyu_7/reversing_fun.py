from itertools import izip_longest


def ReverseFun(n):
    """ reverse_fun == PEP8 (forced CamelCase by CodeWars) """
    half = len(n) / 2
    return ''.join(''.join(a) for a in
                   izip_longest(reversed(n[half:]), n[:half], fillvalue=''))
