from collections import defaultdict


def highest_age(group1, group2):
    max_age = 0
    max_names = []
    total = defaultdict(int)
    for person in group1 + group2:
        name = person['name']
        total[name] += person['age']
        name_total = total[name]
        if name_total > max_age:
            max_names = [name]
            max_age = name_total
        elif name_total == max_age:
            max_names.append(name)
    return min(max_names)
