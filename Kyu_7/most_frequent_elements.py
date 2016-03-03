from collections import Counter


def find_most_frequent(lst):
    maximum = 0
    result = []
    for k, v in Counter(lst).items():
        if v > maximum:
            result = [k]
            maximum = v
        elif v == maximum:
            result.append(k)
    return set(result)

assert find_most_frequent([1, 1, 2, 3]) == {1}
assert find_most_frequent([1, 1, 2, 2, 3]) == {1, 2}
assert find_most_frequent([1, 1, '2', '2', 3]) == {1, '2'}
