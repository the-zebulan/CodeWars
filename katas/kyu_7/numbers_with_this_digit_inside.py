from operator import mul


def numbers_with_digit_inside(x, d):
    num_str = str(d)
    nums = [a for a in xrange(1, x + 1) if num_str in str(a)]
    return [len(nums), sum(nums), reduce(mul, nums) if nums else 0]
