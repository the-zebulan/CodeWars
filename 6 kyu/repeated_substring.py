def f(string):
    length = len(string)
    for a in range(1, length + 1):
        current = string[:a]
        number = length / a
        if current * number == string:
            return current, number

assert f('ababab') == ('ab', 3)
assert f('abcde') == ('abcde', 1)
