def pair_zeros(nums, *_):
    result = []
    skip_zero = False
    for a in nums:
        if a == 0:
            if not skip_zero:
                result.append(a)
            skip_zero = not skip_zero
        else:
            result.append(a)
    return result
