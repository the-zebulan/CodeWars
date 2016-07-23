def maxSequence(arr):
    """ max_sequence == PEP8 (forced mixedCase by CodeWars) """
    maximum = total = 0
    for a in arr:
        total = max(0, total + a)
        if total > maximum:
            maximum = total
    return maximum
