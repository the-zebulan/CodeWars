from collections import defaultdict
from decimal import Decimal


def calculate_improved(students):
    my_dict = defaultdict(list)
    for student in students:
        marks = student['marks']
        beg = marks[0]
        end = marks[-1]
        if len(marks) <= 1 or beg == end or not beg:
            improvement = 0
        elif end is None:
            improvement = -100
        elif beg > end:  # negative improvement
            improvement = round(-100 + Decimal(end) / Decimal(beg) * 100)
        else:            # positive improvement
            beg = Decimal(beg)
            improvement = round((Decimal(end) - beg) / beg * 100)
        my_dict[improvement].append(student['name'])

    return [{'name': student, 'improvement': score}
            for score in sorted(my_dict, reverse=True)
            for student in sorted(my_dict[score])]

students = [
    {'name': 'alex, cow', 'marks': [8, None, None, None, 70, 50, 21, 14]},
    {'name': 'blop, cow', 'marks': [46, 72, 73]},
    {'name': 'whimpy, Johns', 'marks': [None, 1, 99, 24, 81, 64, 95, 39, 88]},
    {'name': 'don, Johns', 'marks': [64]},
    {'name': 'freeman, harold', 'marks': [26, None, 59, 28]},
    {'name': 'master, star', 'marks': [94, 96, 59, 83, 26, 71, 57]},
    {'name': 'joe, plum', 'marks': [None, 0, 85, 8, 82, 58, 81, 32]},
    {'name': 'shaun, Act', 'marks': [24]},
    {'name': 'horse, cow', 'marks': [40, 77, 43]},
    {'name': 'cam, zip', 'marks': [79, 63, 67]},
    {'name': 'jeff, Bug', 'marks': [76, None, 94, 71, 41, 93, 54, None]},
    {'name': 'cat, Johns', 'marks': [94, 94, None, 84, 35, 54, 35, 80]},
    {'name': 'ash, Johns', 'marks': [None, None, 62, None, 27]},
    {'name': 'freeman, willow', 'marks': [67, None, 53]},
    {'name': 'john, Johns', 'marks': [9, 65, None, 66, 75]},
    {'name': 'whimpy, bright', 'marks': [76, 73, None, 81, None, 22, 0]}]

assert calculate_improved(students) == \
    [{'name': 'john, Johns', 'improvement': 733.0},
     {'name': 'alex, cow', 'improvement': 75.0},
     {'name': 'blop, cow', 'improvement': 59.0},
     {'name': 'freeman, harold', 'improvement': 8.0},
     {'name': 'horse, cow', 'improvement': 8.0},
     {'name': 'ash, Johns', 'improvement': 0},
     {'name': 'don, Johns', 'improvement': 0.0},
     {'name': 'joe, plum', 'improvement': 0},
     {'name': 'shaun, Act', 'improvement': 0.0},
     {'name': 'whimpy, Johns', 'improvement': 0},
     {'name': 'cam, zip', 'improvement': -15.0},
     {'name': 'cat, Johns', 'improvement': -15.0},
     {'name': 'freeman, willow', 'improvement': -21.0},
     {'name': 'master, star', 'improvement': -39.0},
     {'name': 'jeff, Bug', 'improvement': -100.0},
     {'name': 'whimpy, bright', 'improvement': -100.0}]

students = [
    {'name': 'santa, luck', 'marks': [31, 17, 51, 29, 70, 80, 28, 19, 96, 11]},
    {'name': 'jeff, zip', 'marks': [91, 43, 79, None, None, 3, 91, None, 39]},
    {'name': 'shaun, harold', 'marks': [None, 50, None, 81, 3, 58, 100, None]},
    {'name': 'blop, fire', 'marks': [65, 42, None, 46, 69, 69, 84, 72, 38]}
]

assert calculate_improved(students) == \
    [{'name': 'shaun, harold', 'improvement': 0},
     {'name': 'blop, fire', 'improvement': -42.0},
     {'name': 'jeff, zip', 'improvement': -57.0},
     {'name': 'santa, luck', 'improvement': -65.0}]

students = [
    {'name': 'Henry, Johns', 'marks': [25, 50]},
    {'name': 'Timmy, Bug', 'marks': [100, 98]},
    {'name': 'George, King', 'marks': [100, 85]},
    {'name': 'Finn, Wish', 'marks': [45, 90]},
    {'name': 'Lucy Act', 'marks': [55, 100]}
]

assert calculate_improved(students) == \
    [{"name":  "Finn, Wish", "improvement": 100},
     {"name": "Henry, Johns", "improvement": 100},
     {"name": "Lucy Act", "improvement": 82},
     {"name": "Timmy, Bug", "improvement": -2},
     {"name": "George, King", "improvement": -15}]

students = [
    {'name': 'Henry, Johns', 'marks': [25, 56, 50]},
    {'name': 'Timmy, Bug', 'marks': [100, 67, 98]},
    {'name': 'George, King', 'marks': [100, 45, 85]},
    {'name': 'Finn, Wish', 'marks': [45, 100, 90]},
    {'name': 'Lucy Act', 'marks': [55, 0, 100]}
]

assert calculate_improved(students) == \
    [{"name": "Finn, Wish", "improvement": 100},
     {"name": "Henry, Johns", "improvement": 100},
     {"name": "Lucy Act", "improvement": 82},
     {"name": "Timmy, Bug", "improvement": -2},
     {"name": "George, King", "improvement": -15}]

students = [
    {'name': 'Henry, Johns', 'marks': [25, 56, 50, 58]},
    {'name': 'Timmy, Bug', 'marks': [100, 67, 98, 100]},
    {'name': 'George, King', 'marks': [100, 45, 85, 90]},
    {'name': 'Finn, Wish', 'marks': [45, 100, 90, 100]},
    {'name': 'Lucy Act', 'marks': [55, 0, 100, 6]}
]

assert calculate_improved(students) == \
    [{"name": "Henry, Johns", "improvement": 132},
     {"name": "Finn, Wish", "improvement": 122},
     {"name": "Timmy, Bug", "improvement": 0},
     {"name": "George, King", "improvement": -10},
     {"name": "Lucy Act", "improvement": -89}]

students = [
    {'name': 'Henry, Johns', 'marks': [0]},
    {'name': 'Timmy, Bug', 'marks': [0]},
    {'name': 'George, King', 'marks': [0]},
    {'name': 'Finn, Wish', 'marks': [0]},
    {'name': 'Lucy Act', 'marks': [0]}
]

assert calculate_improved(students) == \
    [{"name": "Finn, Wish", "improvement": 0},
     {"name": "George, King", "improvement": 0},
     {"name": "Henry, Johns", "improvement": 0},
     {"name": "Lucy Act", "improvement": 0},
     {"name": "Timmy, Bug", "improvement": 0}]

students = [
    {'name': 'Henry, Johns', 'marks': [0, 100]},
    {'name': 'Timmy, Bug', 'marks': [0, 9]},
    {'name': 'George, King', 'marks': [0, 0]},
    {'name': 'Finn, Wish', 'marks': [0, 76]},
    {'name': 'Lucy Act', 'marks': [0, None]}
]

assert calculate_improved(students) == \
    [{"name": "Finn, Wish", "improvement": 0},
     {"name": "George, King", "improvement": 0},
     {"name": "Henry, Johns", "improvement": 0},
     {"name": "Lucy Act", "improvement": 0},
     {"name": "Timmy, Bug", "improvement": 0}]
