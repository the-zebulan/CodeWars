# def solution(number):
#     a = 0
#     b = 0
#     c = 0
#     for d in xrange(1, number):
#         if d % 15 == 0:
#             c += 1
#         elif d % 5 == 0:
#             b += 1
#         elif d % 3 == 0:
#             a += 1
#     return [a, b, c]


def solution(number):
    """ Thanks to 'M.Gaidamaka' from CodeWars """
    number -= 1
    a = number // 3
    b = number // 5
    c = number // 15
    return [a - c, b - c, c]

assert solution(20) == [5, 2, 1]
assert solution(2) == [0, 0, 0]
assert solution(30) == [8, 4, 1]
assert solution(300) == [80, 40, 19]
