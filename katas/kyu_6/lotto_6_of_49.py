from random import randint, sample


def number_generator():
    return sorted(sample(xrange(1, 50), 6)) + [randint(0, 9)]


def check_for_winning_category(your_numbers, winning_numbers):
    superzahl_match = your_numbers.pop() == winning_numbers.pop()
    matches = len(set(your_numbers).intersection(winning_numbers))
    try:
        return {6: 2, 5: 4, 4: 6, 3: 8}[matches] - superzahl_match
    except KeyError:
        return 9 if matches == 2 and superzahl_match else -1
