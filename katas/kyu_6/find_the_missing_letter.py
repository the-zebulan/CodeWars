def find_missing_letter(arr):
    prev = None
    for a in arr:
        current = ord(a)
        if prev is None or current - 1 == prev:
            prev = current
        else:
            return chr(current - 1)
