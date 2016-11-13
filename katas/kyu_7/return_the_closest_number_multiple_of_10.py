def closest_multiple_10(i):
    rem = i % 10
    return i - rem + (10 if rem >= 5 else 0)
