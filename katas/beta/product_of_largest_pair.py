def max_product(nums):
    biggest = second_biggest = 0
    for num in nums:
        gt_second_biggest = num > second_biggest
        if gt_second_biggest and num > biggest:
            second_biggest, biggest = biggest, num
        elif gt_second_biggest:
            second_biggest = num
    return second_biggest * biggest
