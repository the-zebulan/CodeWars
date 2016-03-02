def remove_smallest(n, lst):
    if n <= 0:
        return lst
    elif n > len(lst):
        return []
    dex = [b[1] for b in sorted((a, i) for i, a in enumerate(lst))[:n]]
    return [c for i, c in enumerate(lst) if i not in dex]
