P1_WINS = {'scissorspaper', 'paperrock', 'rockscissors'}


def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    return 'Player {} won!'.format(1 if p1 + p2 in P1_WINS else 2)


assert rps('rock', 'scissors') == 'Player 1 won!'
assert rps('scissors', 'paper') == 'Player 1 won!'
assert rps('paper', 'rock') == 'Player 1 won!'

assert rps('scissors', 'rock') == 'Player 2 won!'
assert rps('paper', 'scissors') == 'Player 2 won!'
assert rps('rock', 'paper') == 'Player 2 won!'

assert rps('rock', 'rock') == 'Draw!'
assert rps('scissors', 'scissors') == 'Draw!'
assert rps('paper', 'paper') == 'Draw!'
