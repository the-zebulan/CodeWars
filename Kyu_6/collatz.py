def collatz(n):
    result = [str(n)]
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3 * n) + 1
        result.append(str(n))
    return '->'.join(result)
