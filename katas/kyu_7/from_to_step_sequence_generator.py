def generator(start, stop, step):
    if step <= 0:
        return []
    elif start > stop:
        step *= -1
        stop -= 2
    return range(start, stop + 1, step)
