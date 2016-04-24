def denumerate(enum_list):
    try:
        nums = dict(enum_list)
        maximum = max(nums) + 1
        result = ''.join(nums[a] for a in xrange(maximum))
        if result.isalnum() and len(result) == maximum:
            return result
    except (KeyError, TypeError, ValueError):
        pass
    return False
