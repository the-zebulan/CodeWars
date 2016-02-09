def in_asc_order(arr):
    return arr == sorted(arr)


assert in_asc_order([1, 2]) is True
assert in_asc_order([2, 1]) is False
assert in_asc_order([1, 2, 3]) is True
assert in_asc_order([1, 3, 2]) is False
assert in_asc_order([1, 4, 13, 97, 508, 1047, 20058]) is True
assert in_asc_order([56, 98, 123, 67, 742, 1024, 32, 90969]) is False
