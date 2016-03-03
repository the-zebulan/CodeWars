def solution(number):
    return sum(a for a in xrange(3, number) if not a % 3 or not a % 5)


assert solution(10) == 23
assert solution(100) == 2318
assert solution(997) == 232169
