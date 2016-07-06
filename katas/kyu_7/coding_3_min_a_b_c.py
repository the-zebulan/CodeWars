from collections import Counter


def find_a_b(numbers, c):
    cnt = Counter(numbers)
    for a in numbers:
        try:
            q, r = divmod(c, a)
        except ZeroDivisionError:
            continue
        nums = cnt[q]
        if r == 0 and (nums > 1 if q == a else nums == 1):
            return [a, q]
