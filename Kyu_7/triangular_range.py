def triangular_range(start, stop):
    cnt = 1
    result = {}
    while True:
        triangle_num = (cnt * (cnt + 1)) / 2
        if start <= triangle_num <= stop:
            result[cnt] = triangle_num
        elif triangle_num > stop:
            return result
        cnt += 1
