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


assert validSolution(
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9, 1],
     [3, 4, 5, 6, 7, 8, 9, 1, 2], [4, 5, 6, 7, 8, 9, 1, 2, 3],
     [5, 6, 7, 8, 9, 1, 2, 3, 4], [6, 7, 8, 9, 1, 2, 3, 4, 5],
     [7, 8, 9, 1, 2, 3, 4, 5, 6], [8, 9, 1, 2, 3, 4, 5, 6, 7],
     [9, 1, 2, 3, 4, 5, 6, 7, 8]]) is False

assert validSolution(
    [[5, 3, 4, 6, 7, 8, 9, 1, 2],
     [6, 7, 2, 1, 9, 5, 3, 4, 8],
     [1, 9, 8, 3, 4, 2, 5, 6, 7],
     [8, 5, 9, 7, 6, 1, 4, 2, 3],
     [4, 2, 6, 8, 5, 3, 7, 9, 1],
     [7, 1, 3, 9, 2, 4, 8, 5, 6],
     [9, 6, 1, 5, 3, 7, 2, 8, 4],
     [2, 8, 7, 4, 1, 9, 6, 3, 5],
     [3, 4, 5, 2, 8, 6, 1, 7, 9]]) is True

assert validSolution(
    [[5, 3, 4, 6, 7, 8, 9, 1, 2],
     [6, 7, 2, 1, 9, 0, 3, 4, 8],
     [1, 0, 0, 3, 4, 2, 5, 6, 0],
     [8, 5, 9, 7, 6, 1, 0, 2, 0],
     [4, 2, 6, 8, 5, 3, 7, 9, 1],
     [7, 1, 3, 9, 2, 4, 8, 5, 6],
     [9, 0, 1, 5, 3, 7, 2, 1, 4],
     [2, 8, 7, 4, 1, 9, 6, 3, 5],
     [3, 0, 0, 4, 8, 1, 1, 7, 9]]) is False
