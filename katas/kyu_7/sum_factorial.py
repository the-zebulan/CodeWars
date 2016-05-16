def sum_factorial(lst):
    nums = sorted(lst)
    current = 1
    total = 0
    for a in xrange(1, nums[-1] + 1):
        current *= a
        if a in nums:
            total += current
    return total


# # repeated values would break the solution above but according to
# # the kata constraints: "Note: Assume that all values in the list are
# # positive integer values > 0 and each value in the list is unique"
# #
# # as an exercise, the code below will solve the problem even
# # with repeated (and positive) nums
# from itertools import groupby
#
#
# def sum_factorial(lst):
#     nums = dict((k, sum(1 for _ in g)) for k, g in groupby(sorted(lst)))
#     current = 1
#     total = 0
#     for a in xrange(1, max(nums) + 1):
#         current *= a
#         total += current * nums.get(a, 0)
#     return total
#
#
# assert sum_factorial([4, 6]) == 744
# assert sum_factorial([5, 4, 1]) == 145
# assert sum_factorial([4, 4, 4]) == 72  # <-- repeated
