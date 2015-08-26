def find_average(nums):
    items = 0
    total = 0.0
    for a in nums:
        items += 1
        total += a
    return 0 if items == 0 else total / items


# def find_average(nums):
    # length = len(nums)
    # return sum(nums) / float(length) if length > 0 else 0

assert find_average([1]) == 1
assert find_average([1, 3, 5, 7]) == 4
assert find_average([-1, 3, 5, -7]) == 0
assert find_average([5, 7, 3, 7]) == 5.5
assert find_average([]) == 0
