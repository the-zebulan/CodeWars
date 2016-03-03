def lowest_product(nums):
    int_nums = []
    length = 0
    for i, a in enumerate(nums, 1):
        int_nums.append(int(a))
        length += 1
    return 'Number is too small' if length < 4 else \
        min(reduce(lambda x, y: x * y, int_nums[b:b + 4])
            for b in xrange(length - 3))


# # second try:
# def lowest_product(nums):
#     int_nums = []
#     for i, a in enumerate(nums, 1):
#         int_nums.append(int(a))
#     else:
#         if i < 4:
#             return 'Number is too small'
#     cnt = 0
#     minimum = None
#     total = 1
#     for i, b in enumerate(int_nums):
#         total *= b
#         if i >= 3:
#             try:
#                 total /= int_nums[cnt]
#                 print total, int_nums[cnt], cnt
#             except ZeroDivisionError:
#                 pass
#             cnt += 1
#             if minimum is None or total < minimum:
#                 minimum = total
#     return minimum
