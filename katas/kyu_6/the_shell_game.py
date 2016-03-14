def find_the_ball(start, swaps):
    for a, b in swaps:
        if a == start:
            start = b
        elif b == start:
            start = a
    return start
