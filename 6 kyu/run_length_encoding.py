from itertools import groupby


def run_length_encoding(string):
    return [[sum(1 for _ in g), k] for k, g in groupby(string)]

assert run_length_encoding('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb') == \
    [[34, 'a'], [3, 'b']]
assert run_length_encoding('') == []
assert run_length_encoding('abc') == [[1, 'a'], [1, 'b'], [1, 'c']]
assert run_length_encoding('aab') == [[2, 'a'], [1, 'b']]
assert run_length_encoding('hello world!') == \
    [[1, 'h'], [1, 'e'], [2, 'l'], [1, 'o'], [1, ' '], [1, 'w'],
     [1, 'o'], [1, 'r'], [1, 'l'], [1, 'd'], [1, '!']]
assert run_length_encoding('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb') == \
    [[34, 'a'], [3, 'b']]
assert run_length_encoding('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWW'
                           'WWBWWWWWWWWWWWWWW') == \
    [[12, 'W'], [1, 'B'], [12, 'W'], [3, 'B'], [24, 'W'], [1, 'B'], [14, 'W']]
