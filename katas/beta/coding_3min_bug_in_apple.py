def sc(apple):
    return next([row, col] for row, a in enumerate(apple)
                for col, b in enumerate(a) if b == 'B')
