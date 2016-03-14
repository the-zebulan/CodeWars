def narcissistic(value):
    num_str = str(value)
    length = len(num_str)
    return sum(int(a) ** length for a in num_str) == value
