WEAPONS = {'Laval': 'Shado Valious', 'Cragger': 'Vengdualize',
           'Lagravis': 'Blazeprowlor', 'Crominus': 'Grandorius',
           'Tormak': 'Tygafyre', 'LiElla': 'Roarburn'}


def identify_weapon(character):
    try:
        return '{}-{}'.format(character, WEAPONS[character])
    except KeyError:
        return 'Not a character'


assert identify_weapon('Laval') == 'Laval-Shado Valious'
assert identify_weapon('A') == 'Not a character'
