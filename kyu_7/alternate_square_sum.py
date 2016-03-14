def alternate_sq_sum(arr):
    return sum(a if i % 2 == 0 else a ** 2 for i, a in enumerate(arr))
