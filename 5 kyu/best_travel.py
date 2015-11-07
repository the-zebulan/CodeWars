from itertools import combinations


def choose_best_sum(max_miles, max_towns, lst):
    highest = 0
    for a in combinations(lst, max_towns):
        total_distance = sum(a)
        if max_miles >= total_distance > highest:
            highest = total_distance
    return highest or None


distances = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123,
             2333, 144, 50, 132, 123, 34, 89]
assert choose_best_sum(230, 4, distances) == 230
assert choose_best_sum(430, 5, distances) == 430
assert choose_best_sum(430, 8, distances) is None
