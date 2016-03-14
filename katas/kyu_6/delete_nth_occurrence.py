from collections import defaultdict


def delete_nth(order, max_e):
    counts = defaultdict(int)
    result = []
    for a in order:
        if counts[a] < max_e:
            result.append(a)
        counts[a] += 1
    return result
