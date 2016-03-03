def find_spaceship(astromap):
    for a, row in enumerate(reversed(astromap.split('\n'))):
        for b, col in enumerate(row):
            if col == 'X':
                return [b, a]
    return 'Spaceship lost forever.'


assert type(find_spaceship('X')) == list
assert find_spaceship('X') == [0, 0]
assert find_spaceship('X\n.') == [0, 1]
assert find_spaceship('.X\n..') == [1, 1]
assert find_spaceship('..\n.X') == [1, 0]
assert find_spaceship('..\nX.') == [0, 0]
assert find_spaceship('.......\nX.......') == [0, 0]
assert find_spaceship(
    '..........\n..........\n.......X..\n..........\n..........') == [7, 2]
assert find_spaceship(
    '..........\n..........\n..........\n........X.\n..........') == [8, 1]
assert type(find_spaceship('')) == str
assert find_spaceship('........................') == 'Spaceship lost forever.'
assert find_spaceship('\n\n\n\n') == 'Spaceship lost forever.'
