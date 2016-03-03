def name_shuffler(name):
    return '{1} {0}'.format(*name.split())


assert name_shuffler('john McClane') == 'McClane john'
assert name_shuffler('Mary jeggins') == 'jeggins Mary'
assert name_shuffler('tom jerry') == 'jerry tom'
