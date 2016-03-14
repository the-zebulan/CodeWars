def noonerize(numbers):
    output = '{}{}'.format
    if any(not isinstance(a, int) for a in numbers):
        return 'invalid array'
    b, c = (str(d) for d in numbers)
    return abs(int(output(c[0], b[1:])) - int(output(b[0], c[1:])))
