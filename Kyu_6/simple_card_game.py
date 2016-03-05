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
