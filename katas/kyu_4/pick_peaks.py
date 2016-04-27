def pick_peaks(arr):
    prev_dex = prev_val = None
    result = {'pos': [], 'peaks': []}
    upwards = False
    for i, a in enumerate(arr):
        if prev_val == a:
            continue
        elif prev_val is None or prev_val < a:
            upwards = True
        else:
            if prev_dex and upwards:
                result['pos'].append(prev_dex)
                result['peaks'].append(prev_val)
            upwards = False
        prev_dex = i
        prev_val = a
    return result
