def two_highest(nums):
    if not nums:
        return []
    elif isinstance(nums, str):
        return False
    return sorted(set(nums), reverse=True)[:2]
