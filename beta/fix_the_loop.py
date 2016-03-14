OUTPUT = '{}. {}\n'.format


def list_animals(animals):
    return ''.join(OUTPUT(i, a) for i, a in enumerate(animals, start=1))
