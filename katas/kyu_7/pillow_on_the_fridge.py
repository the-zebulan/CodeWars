def pillow(arr):
    s1, s2 = arr
    return bool({i for i, a in enumerate(s1) if a == 'n'} &
                {i for i, b in enumerate(s2) if b == 'B'})
