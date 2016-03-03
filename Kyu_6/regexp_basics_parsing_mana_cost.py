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


assert parse_mana_cost('') == {}
assert parse_mana_cost('0') == {}
assert parse_mana_cost('1') == {'*': 1}
assert parse_mana_cost('4') == {'*': 4}
assert parse_mana_cost('15') == {'*': 15}
assert parse_mana_cost('2rr') == {'*': 2, 'r': 2}
assert parse_mana_cost('1wbg') == {'*': 1, 'w': 1, 'b': 1, 'g': 1}
assert parse_mana_cost('1WWU') == {'*': 1, 'w': 2, 'u': 1}
assert parse_mana_cost('0r') == {'r': 1}
assert parse_mana_cost('2x') is None
assert parse_mana_cost('2R') == {'*': 2, 'r': 1}
assert parse_mana_cost('2\n') is None
assert parse_mana_cost('\n2') is None
assert parse_mana_cost('b') == {'b': 1}
