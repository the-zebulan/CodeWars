def expand(maze, fill):
    n = len(maze)
    beg = n / 2
    end = n + beg
    fill_row = [fill for _ in xrange(n * 2)]
    cap = fill_row[:beg]
    maze_iter = iter(maze)
    return [cap + next(maze_iter) + cap if beg <= a < end else fill_row
            for a in xrange(n * 2)]
