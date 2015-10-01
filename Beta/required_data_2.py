def given_nth_value(arr, k, str_):
    if not arr:
        return 'No values in the array'
    if k < 0 or isinstance(k, str):
        return 'Incorrect value for k'
    str_ = str_.lower()
    if str_ not in ('min', 'max'):
        return "Valid entries: 'max' or 'min'"
    try:
        arr = set(int(a) for a in arr)
    except ValueError:
        return 'Invalid entry list'
    if k > len(arr):
        return "No way"
    return sorted(arr, reverse=str_ == 'max')[k - 1]

arr = [3, 3, -1, 10, 6, 8, -5, 4, 22, 31, 34, -16, -16, 8, 8]  # (15 elements)
assert given_nth_value(arr, 5, 'min') == 4
assert given_nth_value(arr, 6, 'max') == 6
assert given_nth_value(arr, 13, 'max') == "No way"

arr = [3, 3, -1, 10, 6, 8, -5, 'Yes', 4, 22, 31]
assert given_nth_value(arr, 4, 'max') == "Invalid entry list"
assert given_nth_value([], 4, 'max') == "No values in the array"

arr = [3, 3, -1, 10, 6, 8, -5, 4, 22, 31]
assert given_nth_value(arr, 2, 'mix') == "Valid entries: 'max' or 'min'"

arr = [3, 3, -1, 10, 6, 8, -5, 4, 22, 31]
assert given_nth_value(arr, 2, 'MaX') == 22
