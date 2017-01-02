def tail_swap(arr):
    fmt = '{}:{}'.format
    (head, tail), (head_2, tail_2) = (a.split(':') for a in arr)
    return [fmt(head, tail_2), fmt(head_2, tail)]
