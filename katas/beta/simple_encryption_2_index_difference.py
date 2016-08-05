from string import ascii_lowercase, ascii_uppercase, digits

VALID_CHARS = '{}{}{}{}'.format(
    ascii_uppercase, ascii_lowercase, digits, ".,:;-?! '()$%&\""
)


def decrypt(encrypted_text):
    if not encrypted_text:
        return encrypted_text
    elif not set(encrypted_text).issubset(VALID_CHARS):
        raise Exception
    result = []
    prev = None
    for a in encrypted_text:
        current = 77 - VALID_CHARS.index(a)
        if prev is None:
            # first character, mirror swap
            prev = VALID_CHARS[current - 1]
        else:
            prev = VALID_CHARS[(VALID_CHARS.index(prev) + current) % 77]
        result.append(prev)
    return ''.join(b.swapcase() if i % 2 else b for i, b in enumerate(result))


def encrypt(text):
    if not text:
        return text
    elif not set(text).issubset(VALID_CHARS):
        raise Exception
    swapped = [a.swapcase() if i % 2 else a for i, a in enumerate(text)]
    result = [VALID_CHARS[-(VALID_CHARS.index(text[0]) + 1)]]
    for b, c in zip(swapped, swapped[1::]):
        dex = (VALID_CHARS.index(b) - VALID_CHARS.index(c)) + 77
        result.append(VALID_CHARS[dex % 77])
    return ''.join(result)
