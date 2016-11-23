def calc(s):
    num = ''.join(str(ord(a)) for a in s)
    num2 = num.replace('7', '1')
    return abs(sum(int(b) for b in num) - sum(int(c) for c in num2))
