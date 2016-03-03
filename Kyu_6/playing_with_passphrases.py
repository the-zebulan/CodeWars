from string import ascii_uppercase as up


def play_pass(string, n):
    result = []
    for i, a in enumerate(string):
        if a.isdigit():
            char = str(9 - int(a))
        elif a.isalpha():
            char = up[(up.index(a) + n) % 26]
            char = char if i % 2 == 0 else char.lower()
        else:
            char = a
        result.append(char)
    return ''.join(reversed(result))

assert play_pass("I LOVE YOU!!!", 1) == "!!!vPz fWpM J"
assert play_pass("MY GRANMA CAME FROM NY ON THE 23RD OF APRIL 2015", 2) == \
       "4897 NkTrC Hq fT67 GjV Pq aP OqTh gOcE CoPcTi aO"
