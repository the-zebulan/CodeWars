from string import ascii_letters as az, maketrans, translate


def caesar_crypto_encode(text, shift):
    if not text:
        return ''
    sh = shift % 52
    return translate(text, maketrans(az, az[sh:] + az[:sh])).strip()
