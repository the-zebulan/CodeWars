def is_sorted_and_how(nums):
    a_or_d = {'a': 'ascending', 'd': 'descending'}
    diffs = {'d' if b - a < 0 else 'a' for a, b in zip(nums, nums[1:])}
    return 'yes, {}'.format(a_or_d[diffs.pop()]) if len(diffs) == 1 else 'no'
