def hotpo(n):
    cnt = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n / 2
        cnt += 1
    return cnt
