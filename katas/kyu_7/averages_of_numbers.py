from operator import truediv


def averages(nums):
    return [truediv(a + b, 2) for a, b in zip(nums, nums[1:])] if nums else []
