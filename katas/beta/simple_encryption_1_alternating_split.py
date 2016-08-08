from itertools import chain, izip_longest


def decrypt(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    half = len(encrypted_text) / 2
    result = encrypted_text
    for _ in xrange(n):
        result = ''.join(chain(*izip_longest(
            result[half:], result[:half], fillvalue=''
        )))
    return result


def encrypt(text, n):
    if not text or n <= 0:
        return text
    result = text
    for _ in xrange(n):
        result = result[1::2] + result[::2]
    return result
