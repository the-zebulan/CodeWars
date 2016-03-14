def better_than_average(class_points, your_points):
    total_students = total_points = 0.0
    for a in class_points:
        total_points += a
        total_students += 1
    return your_points > total_points / total_students
