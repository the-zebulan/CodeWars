def sel_number(n, d):
    cnt = 0
    for a in range(12, n + 1):
        nums = map(int, str(a))
        if nums == sorted(set(nums)) and \
                all(c - b <= d for b, c in zip(nums[:-1], nums[1:])):
            cnt += 1
    return cnt
