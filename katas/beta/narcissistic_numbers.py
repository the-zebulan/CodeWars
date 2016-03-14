def is_narcissistic(n):
    num = str(n)
    length = len(num)
    return sum(int(a) ** length for a in num) == n
