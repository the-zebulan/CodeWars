# def split_workload(workload):
#     left_sum = 0
#     right_sum = sum(workload)
#     minimum = (abs(right_sum), 0)
#     for i, a in enumerate(workload, 1):
#         left_sum += a
#         right_sum -= a
#         current = (abs(right_sum - left_sum), i)
#         if current < minimum:
#             minimum = current
#     return (None, None) if minimum == (0, 0) else minimum[::-1]


def split_workload(workload):
    """ Fork of CrazyMerlyn's solution from CodeWars """
    diff = sum(workload)
    minimum = abs(diff), 0
    for i, work in enumerate(workload, 1):
        diff -= 2 * work
        current = abs(diff), i
        if current < minimum:
            minimum = current
    return (None, None) if minimum == (0, 0) else minimum[::-1]


assert split_workload([1, 6, 2, 3, 5, 4, 1]) == (4, 2)
assert split_workload([]) == (None, None)
