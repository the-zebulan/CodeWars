def sort_array(numbers):
    evens = []
    odds = []
    for a in numbers:
        if a % 2:
            odds.append(a)
            evens.append(None)
        else:
            evens.append(a)
    odds = iter(sorted(odds))
    return [next(odds) if b is None else b for b in evens]
