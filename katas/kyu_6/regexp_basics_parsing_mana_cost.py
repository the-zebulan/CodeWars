from itertools import groupby
from re import compile, match

REGEX = compile(r'(\d*)([wubrg]*)$')


def parse_mana_cost(mana):
    s = mana.lower()
    m = match(REGEX, s)
    if m and s[slice(*m.span())] == s:
        result = {}
        l, r = m.groups()
        try:
            num = int(l)
            if num > 0:
                result['*'] = num
        except ValueError:
            pass
        if r:
            for k, g in groupby(sorted(r)):
                result[k] = sum(1 for _ in g)
        return result
