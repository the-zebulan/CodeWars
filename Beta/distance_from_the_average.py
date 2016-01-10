def distances_from_average(test_list):
    total_sum = total_items = 0.0
    for a in test_list:
        total_items += 1
        total_sum += a
    average = total_sum / total_items
    return [round(average - b, 2) for b in test_list]


assert distances_from_average([55, 95, 62, 36, 48]) == \
       [4.2, -35.8, -2.8, 23.2, 11.2]
assert distances_from_average([1, 1, 1, 1, 1]) == [0, 0, 0, 0, 0]
assert distances_from_average([1, -1, 1, -1, 1, -1]) == \
       [-1.0, 1.0, -1.0, 1.0, -1.0, 1.0]
assert distances_from_average([1, -1, 1, -1, 1]) == \
       [-0.8, 1.2, -0.8, 1.2, -0.8]
assert distances_from_average([2, -2]) == [-2.0, 2.0]
assert distances_from_average([1]) == [0]
assert distances_from_average([123, -65, 32432, -353, -534]) == \
       [6197.6, 6385.6, -26111.4, 6673.6, 6854.6]
assert distances_from_average(xrange(101)) == range(50, -51, -1)
assert distances_from_average(xrange(1001)) == range(500, -501, -1)
assert distances_from_average(xrange(1000001)) == range(500000, -500001, -1)
