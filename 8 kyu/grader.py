GRADE = ((0.9, 'A'), (0.8, 'B'), (0.7, 'C'), (0.6, 'D'))


def grader(score):
    return next(v for k, v in GRADE if score >= k)\
        if 1 >= score >= 0.6 else 'F'

assert grader(0.7) == 'C'
assert grader(0.9) == 'A'
assert grader(0.6) == 'D'
assert grader(-1) == 'F'
