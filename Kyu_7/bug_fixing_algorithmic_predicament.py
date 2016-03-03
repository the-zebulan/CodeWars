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

g1 = [{'name': 'kay', 'age': 1}, {'name': 'john', 'age': 13},
      {'name': 'kay', 'age': 76}]
g2 = [{'name': 'john', 'age': 1}, {'name': 'alice', 'age': 76}]

assert highest_age(g1, [{'name': 'john', 'age': 1},
                        {'name': 'alice', 'age': 77}]) == 'alice'
assert highest_age(g1, g2) == 'kay'
assert highest_age([{'name': 'kay', 'age': 1}, {'name': 'john', 'age': 130},
                    {'name': 'kay', 'age': 76}], g2) == 'john'
assert highest_age([{'name': 'kay', 'age': 1}, {'name': 'john', 'age': 130},
                    {'name': 'kay', 'age': 130}], g2) == 'john'
assert highest_age([{'name': 'kay', 'age': 2}, {'name': 'john', 'age': 130},
                    {'name': 'kay', 'age': 130}], g2) == 'kay'
