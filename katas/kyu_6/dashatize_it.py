def dashatize(num):
    if num is None:
        return 'None'
    prev_has_dash = False
    result = []
    for a in str(abs(num)):
        if int(a) % 2 == 0:
            result.append(a)
            prev_has_dash = False
        else:
            if not prev_has_dash:
                result.append('-')
            result.append(a)
            result.append('-')
            prev_has_dash = True
    return ''.join(result).strip('-')
