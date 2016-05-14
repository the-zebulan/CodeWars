BRACKETS = {'(': ')', '{': '}', '[': ']'}


def validBraces(strng):
    """ valid_braces == PEP8 (forced mixedCase by CodeWars) """
    brackets = []
    for a in strng:
        if a in BRACKETS:
            brackets.append(BRACKETS[a])
            continue
        try:
            if a == brackets.pop():
                continue
        except IndexError:
            pass
        return False
    return not brackets
