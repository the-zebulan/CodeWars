def is_palindrome(string):
    try:
        string = ''.join(a for a in string.lower() if a.isalnum())
        return string == string[::-1]
    except AttributeError:
        return False
