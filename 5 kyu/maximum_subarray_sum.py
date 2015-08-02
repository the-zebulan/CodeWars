def maxSequence(arr):
    """ max_sequence == PEP8, forced camelCase by CodeWars """
    total = 0
    maximum = 0
    for a in arr:
        total += a
        if total < 0:
            total = 0
        if total > maximum:
            maximum = total
    return maximum

assert maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert maxSequence([]) == 0
