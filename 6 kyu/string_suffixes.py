def string_suffix(string):
    total = 0
    for a in range(len(string)):
        for b, c in zip(string, string[a:]):
            if not b == c:
                break
            total += 1
    return total

assert string_suffix('ababaa') == 11
assert string_suffix('abc') == 3
