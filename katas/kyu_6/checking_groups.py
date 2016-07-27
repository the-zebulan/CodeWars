def group_check(s):
    close_brackets = {')': '(', '}': '{', ']': '['}
    open_brackets = []
    for bracket in s:
        if bracket not in close_brackets:
            open_brackets.append(bracket)
            continue
        try:
            if open_brackets.pop() != close_brackets[bracket]:
                return False
        except IndexError:
            return False
    return not open_brackets
