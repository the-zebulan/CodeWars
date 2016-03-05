def validate(n):
    string = str(n)
    mod = 0 if len(string) % 2 == 0 else 1  # 0 for even, 1 for odd
    total = 0
    for i, a in enumerate(string):
        current = int(a)
        if i % 2 == mod:
            double = current * 2
            if double > 9:
                total += double - 9
            else:
                total += double
        else:
            total += current
    return total % 10 == 0
