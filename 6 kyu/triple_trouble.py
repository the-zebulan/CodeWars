def chunks(string, size):
    result = set()
    for a in xrange(len(string) - (size - 1)):
        current = string[a:a + size]
        if len(set(current)) == 1:
            result.add(current[0])
    return result


def triple_double(num1, num2):
    return 1 if chunks(str(num1), 3).intersection(chunks(str(num2), 2)) else 0

assert triple_double(451999277, 41177722899) == 1
assert triple_double(1222345, 12345) == 0
assert triple_double(12345, 12345) == 0
assert triple_double(666789, 12345667) == 1
assert triple_double(10560002, 100) == 1
