def archers_ready(archers):
    return all(a >= 5 for a in archers) if archers else False

assert archers_ready([]) is False
assert archers_ready([1, 2, 3, 4]) is False
assert archers_ready([5, 6, 7, 8]) is True
