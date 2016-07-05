from collections import deque


def int_diff(arr, n):
    nums = deque(sorted(arr))
    result = 0
    while nums:
        plus_n = nums.popleft() + n
        for a in nums:
            if a > plus_n:
                break
            elif a == plus_n:
                result += 1
    return result
