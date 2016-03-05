def chunks(string, size):
    result = set()
    for a in xrange(len(string) - (size - 1)):
        current = string[a:a + size]
        if len(set(current)) == 1:
            result.add(current[0])
    return result


def triple_double(num1, num2):
    return 1 if chunks(str(num1), 3).intersection(chunks(str(num2), 2)) else 0
