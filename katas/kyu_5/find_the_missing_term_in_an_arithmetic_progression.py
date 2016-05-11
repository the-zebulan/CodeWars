def find_missing(nums):
    a, b, c = nums[:3]
    diff = min(b - a, c - b, key=abs)
    for d in nums:
        if d != a:
            return a
        a += diff
