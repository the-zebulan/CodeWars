def is_palindrome(s):
    s = ''.join(a for a in s.lower() if a.isalpha())
    return s == s[::-1]


assert is_palindrome("") is True
assert is_palindrome("maoam") is True
assert is_palindrome("abc") is False
assert is_palindrome("If I had a hi-fi...") is True
