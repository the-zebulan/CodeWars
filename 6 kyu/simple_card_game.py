VALUES = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def winner(deck_steve, deck_josh):
    steve_score = 0
    josh_score = 0
    for s, j in zip((VALUES[a] for a in deck_steve),
                    (VALUES[b] for b in deck_josh)):
        if s > j:
            steve_score += 1
        elif j > s:
            josh_score += 1
    if steve_score == josh_score:
        return 'Tie'
    who_won = 'Steve' if steve_score > josh_score else 'Josh'
    scores = sorted([steve_score, josh_score], reverse=True)
    return '{} wins {} to {}'.format(who_won, *scores)

assert winner(["A", "7", "8"], ["K", "5", "9"]) == 'Steve wins 2 to 1'
assert winner(['K', '2', '4', '5', '4', '3', '2', 'K', 'A', 'T'],
              ['Q', '3', '4', '6', '4', '3', '5', 'A', '8', '7']) \
    == 'Josh wins 4 to 3'
assert winner(['9', 'Q', 'Q', 'A', 'T', '7', '6', '9', '3', 'Q', '4', '3',
               '7', '4', '4', 'Q', '6', '5', '6', '8', 'Q', '8', '4', '8',
               '4', 'A', 'J', 'A', '8', 'J', 'K', '3', '6', 'T', '4', '5',
               '5', '7', 'K', '9'],
              ['T', 'Q', 'K', '2', '8', '4', 'T', 'A', '7', '5', '3', 'A',
               '9', 'K', 'J', '7', '5', '3', '3', '7', 'J', 'Q', 'K', '9',
               'Q', '3', '6', '9', '6', 'K', '7', 'A', 'Q', '2', '7', '5',
               '2', 'A', 'J', '4']) == 'Steve wins 20 to 18'
