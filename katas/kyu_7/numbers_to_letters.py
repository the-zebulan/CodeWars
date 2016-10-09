from string import ascii_lowercase as az


def switcher(arr):
    letters = {i + 1: a for i, a in enumerate(reversed(' ?!' + az))}
    return ''.join(letters.get(int(b), '') for b in arr)
