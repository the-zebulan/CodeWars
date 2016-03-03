from string import maketrans, ascii_lowercase as low, ascii_uppercase as up

TRANSLATION = maketrans(up + low, up[::-1] + low[::-1])


def decode(string):
    return string.translate(TRANSLATION) \
        if isinstance(string, str) else 'Input is not a string'

assert decode("yvvi") == "beer"
assert decode("Blf zoivzwb szw 10 yvvih") == "You already had 10 beers"
assert decode("Ovg'h hdrn rm gsv ulfmgzrm!") == "Let's swim in the fountain!"
assert decode("Tl slnv, blf'iv wifmp") == "Go home, you're drunk"
