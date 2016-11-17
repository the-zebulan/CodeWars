def name_file(fmt, nbr, start):
    if not isinstance(nbr, int) or not isinstance(start, int) or nbr <= 0:
        return []
    filename = fmt.replace('<index_no>', '{0}').format
    return [filename(a) for a in range(start, start + nbr)]
