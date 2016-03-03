def number_of_occurrences(item, lst):
    return lst.count(item)

assert number_of_occurrences(4, []) == 0
assert number_of_occurrences(4, [4, 0, 4]) == 2
assert number_of_occurrences(1024,
                             [1024, 1024, 2056, 512, 256, 4096, 1024]) == 3
assert number_of_occurrences(9, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
assert number_of_occurrences('abc', ['abc', '123', '123', 'abc']) == 2
