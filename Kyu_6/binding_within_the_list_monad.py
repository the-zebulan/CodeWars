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
