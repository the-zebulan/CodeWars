def get_average(marks):
    num_marks = marks_sum = 0
    for mark in marks:
        num_marks += 1
        marks_sum += mark
    return marks_sum / num_marks


assert get_average([2, 2, 2, 2]) == 2
assert get_average([1, 5, 87, 45, 8, 8]) == 25
assert get_average([2, 5, 13, 20, 16, 16, 10]) == 11
assert get_average(
    [1, 2, 15, 15, 17, 11, 12, 17, 17, 14, 13, 15, 6, 11, 8, 7]) == 11
