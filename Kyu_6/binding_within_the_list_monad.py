# def bind(array, func):
#     mapped = map(func, array)
#     result = []
#     for a in mapped:
#         if isinstance(a, list):
#             [result.append(b) for b in a]
#         else:
#             raise TypeError('ERROR! The returned value is not a list!')
#     return result


def bind(lst, func):
    return [a for b in lst for a in func(b)]

assert bind([1, 2, 3], lambda a: [a + 1])
assert bind([1, 2, 3], lambda a: [a]), [1, 2, 3]
assert bind([7, 8, 9], lambda a: [[a]]), [[7], [8], [9]]
assert bind([3, 4, 5], lambda a: [[a, -a]]), [[3, -3], [4, -4], [5, -5]]
assert bind([5, 6, 7], lambda a: [str(a)]), ['5', '6', '7']
