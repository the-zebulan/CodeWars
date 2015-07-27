def find_the_ball(start, swaps):
    for a, b in swaps:
        if a == start:
            start = b
        elif b == start:
            start = a
    return start


assert find_the_ball(5, []) == 5
assert find_the_ball(0, [(0, 1), (2, 1), (0, 1)]) == 2
