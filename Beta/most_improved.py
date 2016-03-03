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
