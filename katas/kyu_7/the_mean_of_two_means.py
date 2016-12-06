from operator import truediv


def mean(arr):
    return truediv(sum(arr), len(arr))


def get_mean(arr, x, y):
    if min(x, y) < 2 or max(x, y) > len(arr):
        return -1
    return truediv(mean(arr[:x]) + mean(arr[-y:]), 2)


# # Python 3
# from statistics import mean
#
#
# def get_mean(arr, x, y):
#     if min(x, y) < 2 or max(x, y) > len(arr):
#         return -1
#     return (mean(arr[:x]) + mean(arr[-y:])) / 2
