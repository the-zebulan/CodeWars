def group_in_10s(*args):
    if not args:
        return []
    args = sorted(args)
    result = [None] * (args[-1] / 10 + 1)
    for arg in args:
        dex = arg / 10
        try:
            result[dex].append(arg)
        except AttributeError:
            result[dex] = [arg]
    return result


assert group_in_10s(1, 2, 3), [[1, 2, 3]]
assert group_in_10s(8, 12, 38, 3, 17, 19, 25, 35, 50) == \
    [[3, 8], [12, 17, 19], [25], [35, 38], None, [50]]
assert group_in_10s(12, 10, 11, 13, 25, 28, 29, 49, 51, 90) == \
    [None, [10, 11, 12, 13], [25, 28, 29], None,
     [49], [51], None, None, None, [90]]
assert group_in_10s() == []
assert group_in_10s(100) == \
    [None, None, None, None, None, None, None, None, None, None, [100]]
