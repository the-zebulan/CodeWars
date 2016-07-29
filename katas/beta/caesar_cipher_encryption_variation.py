from string import ascii_lowercase as az


def caesar_encode(phrase, shift):
    return ' '.join(
        ''.join(az[(az.index(a) + shift + i) % 26] for a in word)
        for i, word in enumerate(phrase.split())
    )
