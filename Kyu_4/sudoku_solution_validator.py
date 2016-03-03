VALID = set(xrange(1, 10))


def validSolution(board):
    """ valid_solution == PEP8 (forced mixedCase by CodeWars)
    :param board: List of lists, 9 x 9 Sudoku grid
    :return: Boolean indicating if the grid is a valid solution
    """
    boxes = [[] for _ in xrange(9)]
    columns = zip(*board)
    for i, row in enumerate(board):
        for col in xrange(3):
            boxes[col + i / 3 * 3].extend(row[col * 3:col * 3 + 3])

    for a in xrange(9):
        if any(b != VALID for b in
               (set(boxes[a]), set(columns[a]), set(board[a]))):
            return False
    return True
