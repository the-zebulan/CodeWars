def digitize(n):
    return map(int, reversed(str(n)))

assert digitize(35231) == [1,3,2,5,3]
