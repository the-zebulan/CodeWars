def isPerfect(n):
    nums = set()
    for a in xrange(1, int(n ** 0.5) + 1):
        q, r = divmod(n, a)
        if not r:
            nums.add(a)
            nums.add(q)
    return sum(nums) - n == n
