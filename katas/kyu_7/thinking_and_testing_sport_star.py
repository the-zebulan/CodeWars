def testit(act, s):
    result = []
    for a, b in zip(act, s):
        if a == 'run':
            result.append(b if b == '_' else '/')
        else:
            result.append(b if b == '|' else 'x')
    return ''.join(result)
