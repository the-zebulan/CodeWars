from collections import deque


def yes_no(arr):
    d = deque(reversed(arr))
    result = []
    while d:
        result.append(d.pop())
        d.rotate()
    return result
