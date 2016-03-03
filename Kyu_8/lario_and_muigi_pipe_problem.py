def pipe_fix(nums):
    return range(nums[0], nums[-1] + 1)


assert pipe_fix([1, 2, 3, 5, 6, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert pipe_fix([1, 2, 3, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
assert pipe_fix([6, 9]) == [6, 7, 8, 9]
assert pipe_fix([-1, 4]) == [-1, 0, 1, 2, 3, 4]
assert pipe_fix([1, 2, 3]) == [1, 2, 3]
