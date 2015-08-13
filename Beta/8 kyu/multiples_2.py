def multiples(x):
    if x % 147 == 0:
        return 'Fang'
    elif x % 7 == 0:
        return 'Fizz'
    elif x % 15 == 0:
        return 'Foo'
    return 'Far'

assert multiples(49) == "Fizz"
assert multiples(147) == "Fang"
assert multiples(30) == "Foo"
assert multiples(51) == "Far"
