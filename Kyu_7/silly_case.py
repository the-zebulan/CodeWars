def sillycase(silly):
    mid = (len(silly) + 1) / 2
    return '{}{}'.format(silly[:mid].lower(), silly[mid:].upper())
