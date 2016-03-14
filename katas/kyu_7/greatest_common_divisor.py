def mygcd(a, b):
    while b:
        a, b = b, a % b
    return a
