from itertools import cycle


def thirt(num):
    while True:
        pattern = cycle((1, 10, 9, 12, 3, 4))
        total = sum(int(a) * pattern.next() for a in reversed(str(num)))
        if total == num:
            return total
        num = total


assert thirt(1234567) == 87
assert thirt(321) == 48
assert thirt(8529) == 79
assert thirt(85299258) == 31
assert thirt(5634) == 57
assert thirt(1111111111) == 71
assert thirt(987654321) == 30
