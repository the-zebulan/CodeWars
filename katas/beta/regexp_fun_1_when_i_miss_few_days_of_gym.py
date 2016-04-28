REPLS = (
    ('probably', 'prolly'), ('Probably', 'Prolly'), ('i am', "i'm"),
    ('I am', "I'm"), ('instagram', 'insta'), ('Instagram', 'Insta'),
    ('do not', "don't"), ('Do not', "Don't"), ('going to', 'gonna'),
    ('Going to', 'Gonna'), ('combination', 'combo'), ('Combination', 'Combo')
)


def gym_slang(s, _=None):
    return reduce(lambda a, kv: a.replace(*kv), REPLS, s)
