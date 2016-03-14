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
