def find_outlier(integers):
    even = odd = None
    e_cnt = o_cnt = 0
    for a in integers:
        if not a % 2:
            even = a
            e_cnt += 1
        else:
            odd = a
            o_cnt += 1
        if e_cnt and o_cnt > 1:
            return even
        elif o_cnt and e_cnt > 1:
            return odd
