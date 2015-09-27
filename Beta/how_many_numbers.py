def sel_number(n, d):
    cnt = 0
    for a in range(12, n + 1):
        nums = map(int, str(a))
        uniq = sorted(set(nums))
        if nums == uniq and all(abs(b - nums[i]) <= d
                                for i, b in enumerate(nums[:-1], 1)):
            cnt += 1
    return cnt

assert sel_number(0, 1) == 0
assert sel_number(3, 1) == 0
assert sel_number(13, 1) == 1  # 12
assert sel_number(20, 2) == 2  # 12, 13
assert sel_number(30, 2) == 4  # 12, 13, 23, 24
assert sel_number(44, 2) == 6  # 12, 13, 23, 24, 34, 35
assert sel_number(50, 3) == 12  # 12 - 14, 23 - 25, 34 - 36, 45 - 47
