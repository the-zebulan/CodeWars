def up_array(arr):
    if arr and all(0 <= a < 10 and isinstance(a, int) for a in arr):
        return [int(c) for c in str(int(''.join(str(b) for b in arr)) + 1)]


assert up_array([2, 3, 9]) == [2, 4, 0]
assert up_array([4, 3, 2, 5]) == [4, 3, 2, 6]
assert up_array([1, -9]) is None
assert up_array([]) is None
