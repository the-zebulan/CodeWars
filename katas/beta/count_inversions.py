from collections import deque


# def count_inversion(nums):  # approx 8.3 seconds per 100,000
#     return sum(a > b for i, a in enumerate(nums) for b in nums[i + 1:])


def count_inversion(nums):  # approx 6.6 seconds per 100,000
    forward_nums = deque(nums)
    result = 0
    for a in nums:
        forward_nums.popleft()
        for b in forward_nums:
            if a > b:
                result += 1
    return result
