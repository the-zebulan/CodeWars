def merge(line):
    length = len(line)
    prev = -1
    result = []
    for i, a in enumerate(line):
        if a == 0:
            continue
        elif prev < 0:
            prev = a
            if length == i + 1:
                result.append(a)
        elif a == prev:
            result.append(a * 2)
            prev = -1
        else:
            result.append(prev)
            prev = a
    return result + [0] * (length - len(result))


# def merge(line):
#     begin = 0
#     length = len(line)
#     result = []
#     for i, a in enumerate(line):
#         if i >= begin:
#             for b in xrange(i + 2, length + 1):
#                 total = sum(line[i:b])
#                 if total == a * 2 and total > 0:
#                     result.append(total)
#                     begin = b
#                     break
#             else:
#                 if a > 0:
#                     result.append(a)
#     return result + [0] * (length - len(result))

assert merge([8, 16, 16, 8]) == [8, 32, 8, 0]
assert merge([2, 0, 0, 0, 2]) == [4, 0, 0, 0, 0]
assert merge([2, 2, 2, 2, 2]) == [4, 4, 2, 0, 0]
assert merge([2, 0, 2, 2]) == [4, 2, 0, 0]
assert merge([2, 0, 2, 4]) == [4, 4, 0, 0]
assert merge([0, 0, 2, 2]) == [4, 0, 0, 0]
