from string import ascii_lowercase as low, ascii_uppercase as up


def encryptor(key, message):
    key %= 26
    result = []
    for a in message:
        if a.islower():
            result.append(low[(low.index(a) + key) % 26])
        elif a.isupper():
            result.append(up[(up.index(a) + key) % 26])
        else:
            result.append(a)
    return ''.join(result)


assert encryptor(13, '') == ''
assert encryptor(13, 'Caesar Cipher') == 'Pnrfne Pvcure'
assert encryptor(-5, 'Hello World!') == 'Czggj Rjmgy!'
assert encryptor(27, 'Whoopi Goldberg') == 'Xippqj Hpmecfsh'
