def bubble(lst):
    length = len(lst) - 1
    result = []
    no_swap = False
    while not no_swap:
        no_swap = True
        for a in range(length):
            if lst[a] > lst[a + 1]:
                lst[a], lst[a + 1] = lst[a + 1], lst[a]
                result.append(list(lst))
                no_swap = False
    return result
