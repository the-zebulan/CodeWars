def collatz(n):
    result = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        result += 1
    return result
