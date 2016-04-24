VALID = {'gravel', 'rock'}


def rake_garden(garden):
    return ' '.join(a if a in VALID else 'gravel' for a in garden.split())
