from collections import defaultdict


def remember(string):
    d = defaultdict(int)
    result = []
    for a in string:
        d[a] += 1
        if d[a] == 2:
            result.append(a)
    return result

assert remember('apple') == ['p']
assert remember('apPle') == []
assert remember('pippi') == ['p', 'i']
assert remember('Pippi') == ['p', 'i']
assert remember('limbojackassin the garden') == ['a', 's', 'i', ' ', 'e', 'n']
assert remember('11pinguin') == ['1', 'i', 'n']
