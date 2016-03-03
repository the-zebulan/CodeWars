def add_binary(a, b):
    return format(a + b, 'b')


assert add_binary(1, 1) == "10"
assert add_binary(0, 1) == "1"
assert add_binary(1, 0) == "1"
assert add_binary(2, 2) == "100"
assert add_binary(51, 12) == "111111"
