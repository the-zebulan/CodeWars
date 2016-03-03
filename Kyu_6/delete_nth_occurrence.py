from collections import defaultdict


def delete_nth(order, max_e):
    counts = defaultdict(int)
    result = []
    for a in order:
        if counts[a] < max_e:
            result.append(a)
        counts[a] += 1
    return result

assert delete_nth([20, 37, 20, 21], 1) == [20, 37, 21]
assert delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]
