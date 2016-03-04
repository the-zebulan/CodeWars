from itertools import combinations


def choose_best_sum(max_miles, max_towns, lst):
    highest = 0
    for a in combinations(lst, max_towns):
        total_distance = sum(a)
        if max_miles >= total_distance > highest:
            highest = total_distance
    return highest or None
