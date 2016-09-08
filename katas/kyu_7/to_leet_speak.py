LEET = {'A': '@', 'B': '8', 'C': '(', 'E': '3', 'G': '6', 'H': '#',
        'I': '!', 'L': '1', 'O': '0', 'S': '$', 'T': '7', 'Z': '2'}


def to_leet_speak(s):
    return ''.join(LEET.get(a, a) for a in s)
