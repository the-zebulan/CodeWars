def better_than_average(class_points, your_points):
    total_students = total_points = 0.0
    for a in class_points:
        total_points += a
        total_students += 1
    return your_points > total_points / total_students


assert better_than_average([2, 3], 5) is True
assert better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75) is True
assert better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69) is True
