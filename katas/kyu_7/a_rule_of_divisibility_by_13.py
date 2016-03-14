from itertools import cycle


def thirt(num):
    while True:
        pattern = cycle((1, 10, 9, 12, 3, 4))
        total = sum(int(a) * pattern.next() for a in reversed(str(num)))
        if total == num:
            return total
        num = total
