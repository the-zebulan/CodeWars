VOWELS = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}


def vowel_2_index(string):
    return ''.join(str(i) if a in VOWELS else a
                   for i, a in enumerate(string, start=1))

assert vowel_2_index('this is my string') == 'th3s 6s my str15ng'
assert vowel_2_index('Codewars is the best site in the world') == 'C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld'
assert vowel_2_index('') == ''
