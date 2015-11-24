VALID = set(xrange(1, 10))


def done_or_not(board):
    boxes = [[] for _ in xrange(9)]
    columns = zip(*board)
    for i, row in enumerate(board):
        for col in xrange(3):
            boxes[col + i / 3 * 3].extend(row[col * 3:col * 3 + 3])

    for a in xrange(9):
        if any(b != VALID for b in
               (set(boxes[a]), set(columns[a]), set(board[a]))):
            return 'Try again!'
    return 'Finished!'


assert done_or_not(
    [[1, 3, 2, 5, 7, 9, 4, 6, 8],
     [4, 9, 8, 2, 6, 1, 3, 7, 5],
     [7, 5, 6, 3, 8, 4, 2, 1, 9],
     [6, 4, 3, 1, 5, 8, 7, 9, 2],
     [5, 2, 1, 7, 9, 3, 8, 4, 6],
     [9, 8, 7, 4, 2, 6, 5, 3, 1],
     [2, 1, 4, 9, 3, 5, 6, 8, 7],
     [3, 6, 5, 8, 1, 7, 9, 2, 4],
     [8, 7, 9, 6, 4, 2, 1, 5, 3]]) == 'Finished!'

assert done_or_not(
    [[1, 3, 2, 5, 7, 9, 4, 6, 8],
     [4, 9, 8, 2, 6, 1, 3, 7, 5],
     [7, 5, 6, 3, 8, 4, 2, 1, 9],
     [6, 4, 3, 1, 5, 8, 7, 9, 2],
     [5, 2, 1, 7, 9, 3, 8, 4, 6],
     [9, 8, 7, 4, 2, 6, 5, 3, 1],
     [2, 1, 4, 9, 3, 5, 6, 8, 7],
     [3, 6, 5, 8, 1, 7, 9, 2, 4],
     [8, 7, 9, 6, 4, 2, 1, 3, 5]]) == 'Try again!'
