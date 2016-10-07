def trim(beard):
    rows = len(beard) - 1
    result = []
    for i, row in enumerate(beard):
        if i < rows:
            result.append(['|' if a == 'J' else a for a in row])
        else:
            result.append(['...' for _ in row])
    return result
