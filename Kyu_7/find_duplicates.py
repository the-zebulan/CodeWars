def duplicates(array):
    seen_before = set()
    result = []
    for a in array:
        if a not in result and a in seen_before:
            result.append(a)
        seen_before.add(a)
    return result

assert duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']) == [4, 3, 1]
assert duplicates([0, 1, 2, 3, 4, 5]) == []
