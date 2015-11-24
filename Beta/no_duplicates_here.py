def list_de_dup(lst):
    return sorted(set(a for a in lst if a is not None)) \
        if isinstance(lst, list) else 'Not an array'


assert list_de_dup(['g', 3, 'a', 'a']) == [3, 'a', 'g']
assert list_de_dup([1, 2, 3, 4, 1, 2, 3, 4]) == [1, 2, 3, 4]
assert list_de_dup(['code', 'wars', 'ain\'t', None, None, 'code', 'wars',
                    'ain\'t', 'the', 'same', 'as', 'the', 'rest']) \
    == ['ain\'t', 'as', 'code', 'rest', 'same', 'the', 'wars']
