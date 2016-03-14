def longest_palindrome(s):
    length = len(s)
    for b in xrange(length, -1, -1):
        cnt = 0
        while cnt + b <= length:
            current = s[cnt:cnt + b]
            if current == current[::-1]:
                return b
            cnt += 1
