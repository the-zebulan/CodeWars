def stringColor(name):
    first_char = other_chars = sum_chars = 0
    prod_chars = 1
    for i, a in enumerate(name):
        current = ord(a)
        if i == 0:
            first_char = current
        else:
            other_chars += current
        prod_chars *= current
        sum_chars += current
    return '{:02X}{:02X}{:02X}'.format(
        sum_chars % 255, prod_chars % 255, abs(first_char - other_chars) % 255
    )
