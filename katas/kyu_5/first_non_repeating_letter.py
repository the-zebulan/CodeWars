from collections import OrderedDict


def first_non_repeating_letter(strng):
    d = OrderedDict()
    for i, a in enumerate(strng.lower()):
        d.setdefault(a, []).append(i)
    return next((strng[v[0]] for v in d.itervalues() if len(v) == 1), '')
