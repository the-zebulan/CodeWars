P1_WINS = {'scissorspaper', 'paperrock', 'rockscissors'}


def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    return 'Player {} won!'.format(1 if p1 + p2 in P1_WINS else 2)
