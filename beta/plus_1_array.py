def up_array(arr):
    if arr and all(0 <= a < 10 and isinstance(a, int) for a in arr):
        return [int(c) for c in str(int(''.join(str(b) for b in arr)) + 1)]
