# def candies(s):  # worst case = three passes of 's', len, max, sum
#     length = len(s)
#     if length <= 1:
#         return -1
#     return max(s) * length - sum(s)


def candies(seq):
    length = 0
    maximum = 0
    total = 0
    for i, a in enumerate(seq):
        try:
            current = int(a)
        except TypeError:
            return -1
        length += 1
        total += current
        if current > maximum:
            maximum = current
    return maximum * length - total if length > 1 else -1
