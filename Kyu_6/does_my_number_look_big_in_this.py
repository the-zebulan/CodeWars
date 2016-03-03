def narcissistic(value):
    num_str = str(value)
    length = len(num_str)
    return sum(int(a) ** length for a in num_str) == value


assert narcissistic(7) is True
assert narcissistic(371) is True
assert narcissistic(122) is False
assert narcissistic(4887) is False
