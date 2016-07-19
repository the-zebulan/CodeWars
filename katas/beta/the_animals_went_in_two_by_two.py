from collections import Counter


def two_by_two(animals):
    if not animals:
        return False
    return {k: 2 for k, v in Counter(animals).items() if v >= 2}
