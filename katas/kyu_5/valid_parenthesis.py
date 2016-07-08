def valid_parentheses(strng):
    open_brackets = 0
    for a in strng:
        if a == '(':
            open_brackets += 1
        elif a == ')':
            open_brackets -= 1
            if open_brackets < 0:
                return False
    return open_brackets == 0
