def sum_factorial(lst):
    nums = sorted(set(lst))
    current = 1
    total = 0
    for a in xrange(1, nums[-1] + 1):
        current *= a
        if a in nums:
            total += current
    return total


assert sum_factorial([4, 6]) == 744
assert sum_factorial([5, 4, 1]) == 145
