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

assert validate(1) is False
assert validate(26) is True
assert validate(91) is True
assert validate(92) is False
assert validate(123) is False
assert validate(1230) is True
assert validate(1714) is False
assert validate(2121) is True
assert validate(912030) is True
assert validate(922030) is False
assert validate(8675309) is False
assert validate(2626262626262626) is True
assert validate(4111111111111111) is True
