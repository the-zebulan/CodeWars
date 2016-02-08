def pipeFix(nums):
    return range(nums[0], nums[-1] + 1)


assert pipeFix([1, 2, 3, 5, 6, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert pipeFix([1, 2, 3, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
assert pipeFix([6, 9]) == [6, 7, 8, 9]
assert pipeFix([-1, 4]) == [-1, 0, 1, 2, 3, 4]
assert pipeFix([1, 2, 3]) == [1, 2, 3]
