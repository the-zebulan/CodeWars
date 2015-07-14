def unique(integers):
    uniq = set()
    result = []
    for a in integers:
        if a not in uniq:
            result.append(a)
        uniq.add(a)
    return result

assert unique([]) == []
assert unique([5, 2, 1, 3]) == [5, 2, 1, 3]
assert unique([1, 5, 2, 0, 2, -3, 1, 10]) == [1, 5, 2, 0, -3, 10]
