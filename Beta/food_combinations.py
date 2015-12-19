OUTPUT = 'You know what\'s actually really good? {}'.format


def actually_really_good(foods):
    foods = list(set(foods))
    length = len(foods)
    if length == 0:
        return OUTPUT('Nothing!')
    return OUTPUT('{} and more {}.'.format(
        foods[0].capitalize(), foods[0 if length == 1 else 1].lower()))


assert actually_really_good([]) == \
    "You know what's actually really good? Nothing!"
assert actually_really_good(['Peanut butter']) == \
    "You know what's actually really good? Peanut butter and more peanut butter."
