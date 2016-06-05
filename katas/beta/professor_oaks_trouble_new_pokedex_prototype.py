class PokeScan(object):
    def __init__(self, name, level, pkmntype):
        self.name = name
        if level <= 20:
            self.level = 'weak'
        elif level <= 50:
            self.level = 'fair'
        else:
            self.level = 'strong'
        self.type = {
            'water': 'wet',
            'fire': 'fiery',
            'grass': 'grassy'
        }[pkmntype]

    def info(self):
        return '{}, a {} and {} Pokemon.'.format(
            self.name, self.type, self.level
        )
