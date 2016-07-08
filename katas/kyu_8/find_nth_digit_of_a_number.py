def find_digit(num, nth):
    if nth <= 0:
        return -1
    try:
        return int(str(num).lstrip('-')[-nth])
    except IndexError:
        return 0
