def distances_from_average(test_list):
    total_sum = total_items = 0.0
    for a in test_list:
        total_items += 1
        total_sum += a
    average = total_sum / total_items
    return [round(average - b, 2) for b in test_list]
