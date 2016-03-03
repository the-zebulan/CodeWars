def get_larger_numbers(a, b):
    return map(max, a, b)


assert get_larger_numbers([13, 64, 15, 17, 88], [23, 14, 53, 17, 80]) \
    == [23, 64, 53, 17, 88]
assert get_larger_numbers([34, -64, 15, 17, 88], [23, 14, 53, 17, 80]) \
    == [34, 14, 53, 17, 88]