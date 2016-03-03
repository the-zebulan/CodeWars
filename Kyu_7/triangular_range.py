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


assert triangular_range(1, 3) == {1: 1, 2: 3}
assert triangular_range(5, 16) == {3: 6, 4: 10, 5: 15}
