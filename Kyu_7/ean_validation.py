def validate_ean(code):
    checksum = int(code[-1])
    total = 0
    for i, a in enumerate(code[:-1]):
        number = int(a)
        if i % 2 != 0:
            number *= 3
        total += number

    total = 0 if total % 10 == 0 else 10 - (total % 10)
    return total == checksum
