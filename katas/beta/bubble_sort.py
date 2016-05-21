def bubble(lst):
    length = len(lst) - 1
    result = []
    no_swap = True
    while True:
        for a in xrange(length):
            if lst[a] > lst[a + 1]:
                lst[a], lst[a + 1] = lst[a + 1], lst[a]
                result.append(list(lst))
                no_swap = False
        if no_swap:
            break
        no_swap = True
    return result
