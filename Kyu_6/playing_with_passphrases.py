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
