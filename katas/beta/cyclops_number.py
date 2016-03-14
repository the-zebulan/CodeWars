def cyclops(n):
    binary = format(n, 'b')
    length = len(binary)
    if not length % 2:
        return False
    return binary[length / 2] == '0' and binary.count('0') == 1
