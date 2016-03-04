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
