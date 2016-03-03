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
