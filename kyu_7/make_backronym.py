DICTIONARY = {'A': 'awesome', 'C': 'confident', 'B': 'beautiful',
              'E': 'eager', 'D': 'disturbing', 'G': 'gregarious',
              'F': 'fantastic', 'I': 'ingestable', 'H': 'hippy',
              'K': 'klingon', 'J': 'joke', 'M': 'mustache', 'L': 'literal',
              'O': 'oscillating', 'N': 'newtonian', 'Q': 'queen',
              'P': 'perfect', 'S': 'stylish', 'R': 'rant', 'U': 'underlying',
              'T': 'turn', 'W': 'weird', 'V': 'volcano', 'Y': 'yogic',
              'X': 'xylophone', 'Z': 'zero'}


def make_backronym(acronym):
    return ' '.join(DICTIONARY[a] for a in acronym.upper())
