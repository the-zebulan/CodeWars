def cyclops(n):
    binary = format(n, 'b')
    length = len(binary)
    if not length % 2:
        return False
    return binary[length / 2] == '0' and binary.count('0') == 1


assert cyclops(1) is False
assert cyclops(5) is True
assert cyclops(3) is False
assert cyclops(13) is False
assert cyclops(27) is True
