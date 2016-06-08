# this global variable is used for testing
# it is forced by the way this kata is written on CodeWars
league_table = [
    ['teamA', 3], ['teamB', 3], ['teamC', 3], ['teamD', 3]
]


def league_calculate(team1, team2, result):
    global league_table
    scores = dict(league_table)
    if result == 'win':
        scores[team1] += 3
    elif result == 'draw':
        scores[team1] += 1
        scores[team2] += 1
    league_table = sorted((list(a) for a in scores.items()),
                          key=lambda b: (-b[1], b[0]))
    return league_table
