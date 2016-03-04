def solution(digits):
    # return max(int(digits[a:a + 5]) for a in xrange(len(digits) - 4))

    # code below only calls int once
    return int(max(digits[a:a + 5] for a in xrange(len(digits) - 4)))
