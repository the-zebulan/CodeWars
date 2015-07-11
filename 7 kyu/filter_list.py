def filter_list(lst):
    return filter(lambda a: isinstance(a, int), lst)

assert filter_list([1, 2, 'a', 'b']) == [1, 2]
assert filter_list([1, 'a', 'b', 0, 15]) == [1, 0, 15]
assert filter_list([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]
