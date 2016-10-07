def array_info(arr):
    if not arr:
        return 'Nothing in the array!'
    int_cnt = float_cnt = str_cnt = space_cnt = 0
    for a in arr:
        if isinstance(a, int):
            int_cnt += 1
        elif isinstance(a, float):
            float_cnt += 1
        elif isinstance(a, str):
            if a.isspace():
                space_cnt += 1
            else:
                str_cnt += 1
    return [
        [len(arr) or None],
        [int_cnt or None],
        [float_cnt or None],
        [str_cnt or None],
        [space_cnt or None]
    ]
