# # # Python 3
# from statistics import mean
#
#
# def average(array):
#     return round(mean(array))


def average(array):
    items = total = 0.0
    for a in array:
        items += 1
        total += a
    return round(total / items)
