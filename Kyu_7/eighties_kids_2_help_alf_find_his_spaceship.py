def find_spaceship(astromap):
    for a, row in enumerate(reversed(astromap.split('\n'))):
        for b, col in enumerate(row):
            if col == 'X':
                return [b, a]
    return 'Spaceship lost forever.'
