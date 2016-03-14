def get_average(marks):
    num_marks = marks_sum = 0
    for mark in marks:
        num_marks += 1
        marks_sum += mark
    return marks_sum / num_marks
