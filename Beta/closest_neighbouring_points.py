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
