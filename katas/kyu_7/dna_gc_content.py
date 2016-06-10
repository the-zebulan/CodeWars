def gc_content(seq):
    if not seq:
        return 0
    gc_cnt = total_chars = 0
    for a in seq:
        if a in 'GC':
            gc_cnt += 1
        total_chars += 1
    return round(100.0 * gc_cnt / total_chars, 2)
