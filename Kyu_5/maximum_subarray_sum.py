def maxSequence(arr):
    """ max_sequence == PEP8 (forced mixedCase by CodeWars) """
    total = 0
    maximum = 0
    for a in arr:
        total += a
        if total < 0:
            total = 0
        if total > maximum:
            maximum = total
    return maximum
