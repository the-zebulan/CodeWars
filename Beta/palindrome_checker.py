def is_palindrome(string):
    try:
        string = ''.join(a for a in string.lower() if a.isalnum())
        return string == string[::-1]
    except AttributeError:
        return False

assert is_palindrome(None) is False
assert is_palindrome('race car') is True
assert is_palindrome('Amor, Roma') is True
assert is_palindrome('aaaaza') is False
assert is_palindrome('No \'x\' in Nixon') is True
