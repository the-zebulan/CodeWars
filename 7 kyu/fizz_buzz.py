def fizzbuzz(n):
    result = []
    for a in xrange(1, n + 1):
        current = ''
        if a % 3 == 0:
            current += 'Fizz'
        if a % 5 == 0:
            current += 'Buzz'
        result.append(current if current else a)
    return result

assert fizzbuzz(10) == [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
