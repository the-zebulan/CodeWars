def hashable(v):
    return set(tuple(a) if isinstance(a, list) else a for a in v)


def match_arrays(v, r):
    return len(hashable(v).intersection(hashable(r)))


assert match_arrays(
    ['Perl', 'Closure', 'JavaScript'], ['Go', 'C++', 'Erlang']) == 0
assert match_arrays(['Erlang', 'JavaScript'], ['Go', 'C++', 'Python']) == 0
assert match_arrays([True, 3, 9, 11, 15], [True, 3, 11]) == 3
