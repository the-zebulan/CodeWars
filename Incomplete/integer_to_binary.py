def to_binary(n):  # negative numbers don't work... YET!
    result = []
    while n != 0:
        n, remainder = divmod(n, 2.0)
        result.append(str(int(remainder)))
    return ''.join(reversed(result))

print(to_binary(253))
print('{:b}'.format(253))
