from math import ceil


def new_avg(arr, average):
    nums_sum = total_nums = 0
    for a in arr:
        nums_sum += a
        total_nums += 1
    donation = ceil((average * (total_nums + 1)) - nums_sum)
    if donation > 0:
        return donation
    raise ValueError
