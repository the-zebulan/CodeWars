from collections import defaultdict


def distance((x, y), (x2, y2)):
    return round(((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5, 4)


def closest_points(points):
    all_points = defaultdict(list)
    total_points = 0
    for i, a in enumerate(points):
        for b in points[i + 1:]:
            all_points[distance(a, b)].append(sorted((a, b)))
        total_points += 1
    minimum_distance, coordinates = min(all_points.items())
    return [total_points, sorted(coordinates), minimum_distance]

assert closest_points([(5, 10), (3, 6), (1, 4), (6, 2),
                       (4, 3), (0, 4), (10, 3), (9, 1)]) \
    == [8, [[(0, 4), (1, 4)]], 1.0]
assert closest_points([(8, 14), (16, 5), (5, 5), (15, 18), (17, 10),
                       (0, 14), (4, 15), (19, 17), (13, 16), (10, 18),
                       (14, 13), (12, 14), (11, 15), (7, 15)]) \
    == [14, [[(7, 15), (8, 14)], [(11, 15), (12, 14)]], 1.4142]
