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


assert new_avg([129306, 37783, 169930, 177970, 66848, 68272, 120258, 10307,
               162807, 54503, 66465, 177701, 144296, 171044, 126332, 144744,
               177657, 61511, 128350, 52167, 103604, 110178, 115495, 97452,
               127971, 36683, 190742, 10960, 183186], 120389.413793) == 387161
assert new_avg([14, 30, 5, 7, 9, 11, 16], 90) == 628
assert new_avg([14, 30, 5, 7, 9, 11, 15], 92) == 645
