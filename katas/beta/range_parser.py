import re


def range_parser(s):
    result = []
    for a in s.split(','):
        nums = [int(b) for b in re.split(r'\D', a) if b]
        if len(nums) == 1:
            result.extend(nums)
        else:
            nums[1] += 1
            result.extend(xrange(*nums))
    return result
