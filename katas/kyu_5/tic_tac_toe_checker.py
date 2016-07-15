from itertools import chain, izip


def isSolved(board):
    """ is_solved == PEP8 (forced mixedCase by CodeWars) """
    cats_game = True
    diagonals = [[], []]
    for i, row in enumerate(board):
        current = set(row)
        if current == {1}:
            return 1
        elif current == {2}:
            return 2
        if cats_game and 0 in current:
            cats_game = False
        diagonals[0].append(row[i])      # nw -> se
        diagonals[1].append(row[2 - i])  # ne -> sw

    for col in chain(izip(*board), diagonals):
        current = set(col)
        if current == {1}:
            return 1
        elif current == {2}:
            return 2
    return 0 if cats_game else -1
