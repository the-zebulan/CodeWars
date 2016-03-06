PLANETS = ('Mercury', 'Venus', 'Earth', 'Mars',
           'Jupiter', 'Saturn', 'Uranus', 'Neptune')


def get_planet_name(planet_id):
    return PLANETS[planet_id - 1]
