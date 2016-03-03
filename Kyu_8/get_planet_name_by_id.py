PLANETS = ('Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune')


def get_planet_name(planet_id):
    return PLANETS[planet_id - 1]

assert get_planet_name(2) == 'Venus'
assert get_planet_name(5) == 'Jupiter'
assert get_planet_name(3) == 'Earth'
assert get_planet_name(4) == 'Mars'
assert get_planet_name(8) == 'Neptune'
assert get_planet_name(1) == 'Mercury'
