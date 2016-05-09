def swap(matrix, row1, row2, *columns):
    result = list(matrix)
    for a in columns:
        result[row1][a], result[row2][a] = result[row2][a], result[row1][a]
    return result
