def solution(nums):
    return sorted(nums) if isinstance(nums, (list, tuple)) else []

assert solution([1, 2, 10, 5]) == [1, 2, 5, 10]
assert solution((1, 2, 10, 5)) == [1, 2, 5, 10]
