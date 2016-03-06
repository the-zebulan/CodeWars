VOWELS = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}


def vowel_2_index(string):
    return ''.join(str(i) if a in VOWELS else a
                   for i, a in enumerate(string, start=1))
