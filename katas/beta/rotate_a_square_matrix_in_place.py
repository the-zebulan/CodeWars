def rotate_in_place(matrix):
    for r, row in enumerate(zip(*matrix)):
        for c, col in enumerate(reversed(row)):
            matrix[r][c] = col
    return matrix
