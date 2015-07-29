def hamming(a, b):
    return sum(c != d for c, d in zip(a, b))

assert hamming('I like turtles', 'I like turkeys') == 3
assert hamming('Hello World', 'Hello World') == 0
