def solution(number):
    return sum(a for a in xrange(3, number) if not a % 3 or not a % 5)
