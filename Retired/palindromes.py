def is_palindrome(s):
    s = ''.join(a for a in s.lower() if a.isalpha())
    return s == s[::-1]
